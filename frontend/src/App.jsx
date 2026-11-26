import { useEffect, useState } from "react";
import "./App.css";

const API = "http://127.0.0.1:8000";

function App() {
  const [page, setPage] = useState("home");
  const [events, setEvents] = useState([]);
  const [user, setUser] = useState(null);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const [interests, setInterests] = useState("");
  const [recommendations, setRecommendations] = useState([]);

  const [registerData, setRegisterData] = useState({
    name: "",
    email: "",
    password: ""
  });

  const [loginData, setLoginData] = useState({
    email: "",
    password: ""
  });

  const [eventData, setEventData] = useState({
    title: "",
    description: "",
    date: "",
    venue: ""
  });

  const [eventId, setEventId] = useState("");
  const [registrationId, setRegistrationId] = useState("");

  useEffect(() => {
    loadEvents();
  }, []);

  async function loadEvents() {
    try {
      const response = await fetch(`${API}/events`);
      if (!response.ok) throw new Error("Could not load events");
      const data = await response.json();
      setEvents(data);
    } catch (error) {
      setMessage("Unable to connect to backend. Please start the FastAPI server.");
    }
  }

  async function handleRecommendations(e) {
    e.preventDefault();
    setLoading(true);
    setMessage("");
    setRecommendations([]);

    try {
      const query = new URLSearchParams({
        interests: interests
      });

      const response = await fetch(
        `${API}/recommend-events?${query.toString()}`
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Could not get recommendations");
      }

      setRecommendations(data.recommendations || []);

      if (!data.recommendations || data.recommendations.length === 0) {
        setMessage("No matching events found. Try different interests.");
      } else {
        setMessage("AI recommendations generated successfully!");
      }
    } catch (error) {
      setMessage(error.message);
    } finally {
      setLoading(false);
    }
  }

  async function handleRegister(e) {
    e.preventDefault();
    setLoading(true);
    setMessage("");

    try {
      const response = await fetch(`${API}/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(registerData)
      });

      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || "Registration failed");

      setMessage("Registration successful! Please log in.");
      setRegisterData({ name: "", email: "", password: "" });
      setPage("login");
    } catch (error) {
      setMessage(error.message);
    } finally {
      setLoading(false);
    }
  }

  async function handleLogin(e) {
    e.preventDefault();
    setLoading(true);
    setMessage("");

    try {
      const response = await fetch(`${API}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(loginData)
      });

      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || "Login failed");

      setUser(data);
      setMessage(`Welcome, ${data.name}!`);
      setLoginData({ email: "", password: "" });
      setPage("events");
    } catch (error) {
      setMessage(error.message);
    } finally {
      setLoading(false);
    }
  }

  async function handleCreateEvent(e) {
    e.preventDefault();
    setLoading(true);
    setMessage("");

    try {
      const response = await fetch(`${API}/events`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(eventData)
      });

      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || "Event creation failed");

      setMessage("Event created successfully!");
      setEventData({
        title: "",
        description: "",
        date: "",
        venue: ""
      });
      await loadEvents();
      setPage("events");
    } catch (error) {
      setMessage(error.message);
    } finally {
      setLoading(false);
    }
  }

  async function handleEventRegistration(e) {
    e.preventDefault();

    if (!user) {
      setMessage("Please log in before registering for an event.");
      setPage("login");
      return;
    }

    setLoading(true);
    setMessage("");

    try {
      const response = await fetch(`${API}/event-register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          user_id: user.user_id,
          event_id: Number(eventId)
        })
      });

      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || "Event registration failed");

      setRegistrationId(String(data.registration_id));
      setMessage(`Successfully registered! Your registration ID is ${data.registration_id}.`);
      setPage("attendance");
    } catch (error) {
      setMessage(error.message);
    } finally {
      setLoading(false);
    }
  }

  async function handleAttendance(e) {
    e.preventDefault();
    setLoading(true);
    setMessage("");

    try {
      const response = await fetch(`${API}/attendance`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          registration_id: Number(registrationId),
          status: "Present"
        })
      });

      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || "Attendance marking failed");

      setMessage("Attendance marked successfully!");
    } catch (error) {
      setMessage(error.message);
    } finally {
      setLoading(false);
    }
  }

  function logout() {
    setUser(null);
    setPage("home");
    setMessage("You have logged out successfully.");
  }

  return (
    <div className="app">
      <header className="navbar">
        <div className="brand" onClick={() => setPage("home")}>
          <span className="brand-icon">✦</span>
          Event<span>Sphere</span>
        </div>

        <nav>
          <button onClick={() => setPage("home")}>Home</button>
          <button onClick={() => { loadEvents(); setPage("events"); }}>
            Events
          </button>
          <button onClick={() => setPage("ai-recommendations")}>
            AI Recommendations
          </button>
          <button onClick={() => setPage("create-event")}>Create Event</button>
          <button onClick={() => setPage("attendance")}>Attendance</button>
        </nav>

        <div className="nav-account">
          {user ? (
            <>
              <span className="welcome-user">Hi, {user.name}</span>
              <button className="nav-login" onClick={logout}>Logout</button>
            </>
          ) : (
            <>
              <button onClick={() => setPage("login")}>Login</button>
              <button className="nav-login" onClick={() => setPage("register")}>
                Sign Up
              </button>
            </>
          )}
        </div>
      </header>

      <main>
        {message && (
          <div className="message">
            {message}
            <button onClick={() => setMessage("")}>×</button>
          </div>
        )}

        {page === "home" && (
          <section className="hero">
            <div className="hero-content">
              <p className="eyebrow">SMART EVENT MANAGEMENT PLATFORM</p>
              <h1>Plan Better.<br />Connect Smarter.</h1>
              <p className="hero-description">
                Discover events, manage registrations, organize schedules
                and track attendance — all in one place.
              </p>
              <div className="hero-actions">
                <button className="primary-button" onClick={() => setPage("events")}>
                  Explore Events →
                </button>
                <button className="secondary-button" onClick={() => setPage("register")}>
                  Get Started
                </button>
                <button className="secondary-button" onClick={() => setPage("ai-recommendations")}>
                  Explore AI →
                </button>
              </div>
            </div>

            <div className="hero-art">
              <div className="art-circle">✦</div>
              <div className="art-card">
                <span>✧</span>
                <h2>EVENTS</h2>
                <p>Ideas become experiences.</p>
              </div>
              <div className="art-small">✦ Connect · Create · Celebrate</div>
            </div>
          </section>
        )}

        {page === "register" && (
          <section className="form-section">
            <h1>Create Your Account</h1>
            <p>Join our smart event community.</p>
            <form onSubmit={handleRegister} className="form-card">
              <label>Full Name</label>
              <input required value={registerData.name}
                onChange={e => setRegisterData({...registerData, name: e.target.value})}
                placeholder="Enter your name" />

              <label>Email Address</label>
              <input required type="email" value={registerData.email}
                onChange={e => setRegisterData({...registerData, email: e.target.value})}
                placeholder="Enter your email" />

              <label>Password (minimum 8 characters)</label>
              <input required minLength="8" type="password" value={registerData.password}
                onChange={e => setRegisterData({...registerData, password: e.target.value})}
                placeholder="Create a password" />

              <button className="primary-button full-button" disabled={loading}>
                {loading ? "Please wait..." : "Create Account"}
              </button>
              <p className="form-bottom">
                Already registered? <button type="button" onClick={() => setPage("login")}>Login</button>
              </p>
            </form>
          </section>
        )}

        {page === "login" && (
          <section className="form-section">
            <h1>Welcome Back!</h1>
            <p>Log in to continue your event journey.</p>
            <form onSubmit={handleLogin} className="form-card">
              <label>Email Address</label>
              <input required type="email" value={loginData.email}
                onChange={e => setLoginData({...loginData, email: e.target.value})}
                placeholder="Enter your email" />

              <label>Password</label>
              <input required type="password" value={loginData.password}
                onChange={e => setLoginData({...loginData, password: e.target.value})}
                placeholder="Enter your password" />

              <button className="primary-button full-button" disabled={loading}>
                {loading ? "Please wait..." : "Login"}
              </button>
              <p className="form-bottom">
                New here? <button type="button" onClick={() => setPage("register")}>Create an account</button>
              </p>
            </form>
          </section>
        )}

        {page === "events" && (
          <section className="content-section">
            <div className="section-heading">
              <p className="eyebrow">DISCOVER EXPERIENCES</p>
              <h1>Upcoming Events</h1>
              <p>Find an event and reserve your place.</p>
            </div>

            <div className="event-grid">
              {events.length === 0 ? (
                <p className="empty-state">No events available yet. Create your first event!</p>
              ) : (
                events.map(event => (
                  <article className="event-card" key={event.id}>
                    <div className="event-image">✦</div>
                    <div className="event-details">
                      <span className="event-tag">EVENT #{event.id}</span>
                      <h2>{event.title}</h2>
                      <p>{event.description}</p>
                      <div className="event-info">📅 {event.date}</div>
                      <div className="event-info">📍 {event.venue}</div>
                      <button className="primary-button full-button"
                        onClick={() => {
                          setEventId(String(event.id));
                          setPage("event-register");
                        }}>
                        Register for Event
                      </button>
                    </div>
                  </article>
                ))
              )}
            </div>
            <button className="secondary-button refresh-button" onClick={loadEvents}>
              Refresh Events
            </button>
          </section>
        )}

        {page === "ai-recommendations" && (
          <section className="content-section">
            <div className="section-heading">
              <p className="eyebrow">POWERED BY MACHINE LEARNING</p>
              <h1>AI Event Recommendations</h1>
              <p>Tell us what you are interested in. Our AI will find matching events.</p>
            </div>

            <form className="form-card" onSubmit={handleRecommendations}>
              <label>Your Interests</label>
              <textarea
                required
                value={interests}
                onChange={e => setInterests(e.target.value)}
                placeholder="Example: Python, Artificial Intelligence, Machine Learning"
              />
              <button className="primary-button full-button" disabled={loading}>
                {loading ? "Finding Events..." : "Get AI Recommendations"}
              </button>
            </form>

            {recommendations.length > 0 && (
              <div className="event-grid">
                {recommendations.map(event => (
                  <article className="event-card" key={event.id}>
                    <div className="event-image">✦ AI MATCH</div>
                    <div className="event-details">
                      <span className="event-tag">
                        {event.match_score}% MATCH
                      </span>
                      <h2>{event.title}</h2>
                      <p>{event.description}</p>
                      <div className="event-info">📅 {event.date}</div>
                      <div className="event-info">📍 {event.venue}</div>
                      <button
                        className="primary-button full-button"
                        onClick={() => {
                          setEventId(String(event.id));
                          setPage("event-register");
                        }}
                      >
                        Register for Event
                      </button>
                    </div>
                  </article>
                ))}
              </div>
            )}
          </section>
        )}

        {page === "create-event" && (
          <section className="form-section">
            <h1>Create a New Event</h1>
            <p>Add an event to the platform.</p>
            <form onSubmit={handleCreateEvent} className="form-card">
              <label>Event Title</label>
              <input required value={eventData.title}
                onChange={e => setEventData({...eventData, title: e.target.value})}
                placeholder="Enter event title" />

              <label>Description</label>
              <textarea required value={eventData.description}
                onChange={e => setEventData({...eventData, description: e.target.value})}
                placeholder="Describe your event" />

              <label>Date</label>
              <input required type="date" value={eventData.date}
                onChange={e => setEventData({...eventData, date: e.target.value})} />

              <label>Venue</label>
              <input required value={eventData.venue}
                onChange={e => setEventData({...eventData, venue: e.target.value})}
                placeholder="Enter event venue" />

              <button className="primary-button full-button" disabled={loading}>
                {loading ? "Creating..." : "Create Event"}
              </button>
            </form>
          </section>
        )}

        {page === "event-register" && (
          <section className="form-section">
            <h1>Event Registration</h1>
            <p>Confirm your event registration.</p>
            <form onSubmit={handleEventRegistration} className="form-card">
              <label>Event ID</label>
              <input required type="number" min="1" value={eventId}
                onChange={e => setEventId(e.target.value)} />
              <button className="primary-button full-button" disabled={loading || !user}>
                {loading ? "Registering..." : "Confirm Registration"}
              </button>
              {!user && <p className="form-note">Please log in before registering.</p>}
            </form>
          </section>
        )}

        {page === "attendance" && (
          <section className="form-section">
            <h1>Attendance Management</h1>
            <p>Mark attendance using your registration ID.</p>
            <form onSubmit={handleAttendance} className="form-card">
              <label>Registration ID</label>
              <input required type="number" min="1" value={registrationId}
                onChange={e => setRegistrationId(e.target.value)}
                placeholder="Enter registration ID" />
              <button className="primary-button full-button" disabled={loading}>
                {loading ? "Submitting..." : "Mark Present"}
              </button>
            </form>
          </section>
        )}
      </main>

      <footer className="footer">
        <h2>EventSphere</h2>
        <p>Smart planning. Better experiences. Stronger connections.</p>
        <p>© 2026 Smart Event Management Platform</p>
      </footer>
    </div>
  );
}

export default App;