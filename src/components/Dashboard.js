import React, { Component, Fragment } from 'react'
import avatar from "../images/profile-image.png"
import parkingAvatar from "../images/parking-placeholder.png"
import {handleShowModal, handleHideModal} from "../actions/modal"
import {handleGetUserDetails} from "../actions/AuthedUser"
import { connect } from 'react-redux'
import {handleGetParkings} from "../actions/parkings"
import jwt from "jsonwebtoken"
import {loginSuccess, handleLogin} from "../actions/AuthedUser"
import * as Api from "../components/Api"


class Dashboard extends Component {
  constructor(props) {
    super(props)
    this.state = {
      loading: this.props.AuthedUser.parkings,
      listedParking: true,
    }
  }
  testEvent = (e) => {
    e.preventDefault()
    console.log(e)
  }
  componentWillMount() {
    const {dispatch} = this.props
    dispatch(handleHideModal())
  }
  componentDidMount() {
    const {dispatch} = this.props
    const user = (jwt.decode(localStorage.auth))
  }
  handleChange = (e) => {
   let value = document.getElementById("contact").textContent
   let name = e.target.name
   this.setState((state) => ({
     contact: value,
   }))
   console.log(this.state.contact)
   console.log(e)
 }

 save = () => {
   let value = document.getElementById("contact").textContent
   console.log(value)
 }
 //
 // componentDidMount() {
 //   const {dispatch} = this.props
 //   dispatch(handleGetUserDetails())
 // }

 getUserParkings = () => {
   const {AuthedUser, parkings} = this.props
   let newParkings = []
  let parkingList = AuthedUser.cars.map(car => {
    newParkings.push(parkings[car.id])
  })
  console.log("newparkings: ")
  console.log(newParkings)
 }

 toggleNav = () => {
   this.setState({
     listedParking: !this.state.listedParking,
   })
 }

  render() {

    const {AuthedUser} = this.props
    if (AuthedUser.cars) {
      this.getUserParkings()
    }
    return (
      <Fragment>
        {AuthedUser &&
          <div className="grey-background">
            <div className="dashboard main-container">
              <div className="user white-background">
                <div className="avatar main-container">
                  <img src={avatar}></img>
                  <h3 contenteditable="true">{AuthedUser.first_name}</h3>
                  <p>Serdang, Selangor</p>
                </div>
                <div className="contact container">
                  <h5>Contact Information</h5>
                  <div><img></img><span name="contact" id="contact" onInput={this.handleChange} contenteditable="true" value={this.state.contact}>{AuthedUser.contact}</span></div>
                  <div><img></img><span>{AuthedUser.email}</span></div>
                </div>
              </div>
              <div className="parking">
                <div className="white-background">
                  <div className="navigation container">
                    <button onClick={this.toggleNav} disabled={this.state.listedParking}>Listed Parking</button>
                    <button onClick={this.toggleNav} disabled={!this.state.listedParking}>Rented Parking</button>
                  </div>
                </div>
                {AuthedUser.parkings &&
                  <div className="listing">
                    {this.state.listedParking
                      ? <ListedParking AuthedUser={AuthedUser}/>
                      : <RentedParking AuthedUser={AuthedUser} parkings={this.props.parkings}/>
                    }
                  </div>
                }
              </div>
            </div>
          </div>
        }
      </Fragment>
    )
  }
}

const ListedParking = (props) => (
  <ul>
    {props.AuthedUser.parkings.map(parking =>
      <li>
        <div className="listing-container white-background">
          <div className="thumbnail">
            <img src={parkingAvatar}></img>
          </div>
          <div className="details-container">
            <div className="name">
              <h3>{parking.db_property}</h3>
              <p>Lot B 13-1</p>
            </div>
            <div className="details">
              <div>
                <h5>Vehicle Registered</h5>
                <p>ABC 7364</p>
              </div>
              <div>
                <h5>Rental</h5>
                <p>RM{parking.db_price}</p>
              </div>
              <div>
                <h5>User Registered</h5>
                <p>Clamone Parkinson</p>
              </div>
            </div>
          </div>
        </div>
      </li>
    )}
  </ul>
)

const RentedParking = (props) => (
  <ul>
    {props.AuthedUser.cars.map(car =>
      <li>
        <div className="listing-container white-background">
          <div className="thumbnail">
            <img src={parkingAvatar}></img>
          </div>
          <div className="details-container">
            <div className="name">
              <h3>{props.parkings[car.id].db_property}</h3>
              <p>Lot B 13-1</p>
            </div>
            <div className="details">
              <div>
                <h5>Vehicle Registered</h5>
                <p>ABC 7364</p>
              </div>
              <div>
                <h5>Rental</h5>
                <p>RM{props.parkings[car.id].db_price}</p>
              </div>
              <div>
                <h5>User Registered</h5>
                <p>Clamone Parkinson</p>
              </div>
            </div>
          </div>
        </div>
      </li>
    )}
  </ul>
)

function mapStateToProps({AuthedUser, modal, parkings}) {
  return {
    modal,
    AuthedUser,
    parkings
  }
}
export default connect(mapStateToProps)(Dashboard)
