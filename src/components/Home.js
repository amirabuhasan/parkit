import React, { Component } from 'react';
import { Link } from 'react-router-dom'
import { connect } from "react-redux"
import { Redirect } from "react-router-dom"
import MetaTags from 'react-meta-tags'

import hero1 from "../images/hero-image1.png"
import hero2 from "../images/hero-image2.png"
import hero3 from "../images/hero-image3.png"
import hero4 from "../images/hero-image4.png"
import logos from "../images/logos.png"
import cloud from "../images/clouds.png"
import {handleShowModal} from "../actions/modal"
import Button from "./common/Button";

class Home extends Component {
  openModalRegister = () => {
    console.log("yes")
    const {dispatch} = this.props
    dispatch(handleShowModal("Register"))
  }
  render() {
    const {AuthedUser} = this.props
    // if (AuthedUser) {
    //   return <Redirect to={"/dashboard"} />
    // }

    return (
      <div className="landing home white-background ">
        <MetaTags>
          <title>Parkit</title>
          <meta name="description" content="In the business of solving Malaysia's parking problem. 
            We help home owners rent out and manage their empty parking spaces to drivers who are in need. 
            Available all across Klang Valley." />
          <meta property="og:title" content="Home | ParkIt | Parking rental services" />
          <meta property="og:image" />
        </MetaTags>
        <section className="hero one background-grey full-width-main">
          <div className="content">
            <h1><span>Connecting</span> drivers to unused parking spaces</h1>
            <p>It's easier than building new ones. Park with ParkIt for all your parking needs.</p>
          </div>
          <div className="full-width">
            <img className="hero-img" src={hero1}></img>
          </div>
        </section>
        <section className="hero two full-width">
          <img className="hero-img" src={hero2}></img>
          <div className="content">
            <h1>Your dedicated parking buddy</h1>
            <p>
              Parking in our city has always been difficult; either time consuming,
              expensive or both.
            </p>
            <p>
              Parkit solves this by providing you
              affordable and convenient parking spaces
              in residential and commercial hot spots.
            </p>
          </div>
        </section>
        <section className="hero three full-width">
          <div className="content">
            <img className="cloud" src={cloud}></img>
            <h1>Looking for a parking space?</h1>
            <p>
              Search and book from our available parking spaces now!
            </p>
            <Link to="/find-parking/search">
              <Button buttonText="I NEED A PARKING" />
            </Link>
          </div>
          <img className="hero-img" src={hero3}></img>
        </section>
        <section className="hero four full-width">
          <img className="hero-img" src={hero4}></img>
          <div className="content">
            <img className="cloud" src={cloud}></img>
            <h1>Want to rent out your parking space?</h1>
            <p>
              Fill up our form and rent your parking space on ParkIt today!
            </p>
            <Link to="/add-listing">
              <Button buttonText="I HAVE A PARKING" />
            </Link>
          </div>
        </section>
        <section className="signup">
          <div className="full-width">
            <h3>We're here for all your parking needs. Sign up now!</h3>
            <Button 
              onClick={this.openModalRegister}
              buttonText="GET STARTED"
            />
          </div>
        </section>
        <section className="partners">
          <div className="logo-container">
            <img className="logo" src={logos}></img>
          </div>
        </section>
      </div>

    )
  }
}

function mapStateToProps({modal, AuthedUser}) {
  return {
    modal,
    AuthedUser
  }
}

export default connect(mapStateToProps)(Home)
