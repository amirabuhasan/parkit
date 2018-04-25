import React, { Component } from 'react';
import {BrowserRouter as Router, Route} from "react-router-dom"
import LoginRegisterHeader from "./LoginRegisterHeader"
import { Link } from 'react-router-dom'
import * as Api from "./Api"

class Login extends Component {
  constructor(props) {
    super(props)
    this.state = {
      IsAuthenticated: null
    }
  }

  handleChange = (e) => {
    let value = e.target.value
    let name = e.target.name
    this.setState((state) => ({
      [name]: value
    }))
  }

  handleSubmit = (e) => {
    e.preventDefault()
    let data = this.state
    Api.login(data).then(response => {
      const key = response.key
      localStorage.setItem("auth", key)
      this.setState({ IsAuthenticated: key })
    })
    console.log(localStorage.auth)
  }

  logout = () => {
    localStorage.removeItem("auth")
    this.setState({ IsAuthenticated: null })
    console.log(localStorage)
  }

  render() {
    return(
      <div className="login-register-container container">
        <LoginRegisterHeader />
        <div className="login-register-form-container">
          <h3 className="login-register-form-header">Log In</h3>
          <form className="login-register-form-content" onSubmit={this.handleSubmit}>
            <label>
              Username
            </label>
            <input
              name="username"
              className="login-register-form-input"
              type="text"
              value={this.state.value}
              onChange={this.handleChange}
              >
            </input>
            <label>
              Email
            </label>
            <input
              name="email"
              className="login-register-form-input"
              type="text"
              value={this.state.value}
              onChange={this.handleChange}
              >
            </input>
            <label>
              Password:
            </label>
            <input
              name="password"
              className="login-register-form-input"
              type="text"
              value={this.state.value}
              onChange={this.handleChange}
              >
            </input>
            <p><a>Forgot Password?</a></p>
            <button className="btn login-register-button">Log In</button>
            <p>Don't have an account? <Link to="/register">Sign up</Link> here.</p>
          </form>
        </div>
        {(localStorage.auth ?
          <div onClick={this.logout}>Logout</div>
          : <div>No</div>
        )}
      </div>
    )
  }
}

class Register extends Component {
  render() {
    return(
      <div className="login-register-form-container">
        <h3 className="login-register-form-header">Register</h3>
        <form className="login-register-form-content">
          <label>
            First Name:
          </label>
          <input className="login-register-form-input" type="text"></input>
          <label>
            Last Name:
          </label>
          <input className="login-register-form-input" type="text"></input>
          <label>
            Email:
          </label>
          <input className="login-register-form-input" type="text"></input>
          <label>
            Contact No:
          </label>
          <input className="login-register-form-input" type="text"></input>
          <label>
            Password:
          </label>
          <input className="login-register-form-input" type="text"></input>
          <label>
            Confirm Password:
          </label>
          <input className="login-register-form-input" type="text"></input>
          <button className="btn">Register</button>
          <p className="footer-text">Already have an account? <a>Login</a> here.</p>
        </form>
      </div>
    )
  }
}

export default Login
