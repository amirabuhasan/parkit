import React, { Component } from 'react';

class ThankYou extends Component {
  render() {
    return(
      <div className="add-listing-container thank-you container image-background">
        <div className="add-listing-form-container thank-you">
          <div className="add-listing-form-content thank-you">
            <div className="add-listing-form-header thank-you">
              <h1>
                Much Appreciated!
              </h1>
            </div>
            <div className="add-listing-form-body thank-you">
              <div>
                <h4>Thank you Jao Ern for leasing out your carpark with ParkIt.</h4>
              </div>
            </div>
            <div className="add-listing-form-body thank-you">
              <div>
                <p>A confirmation email has been sent to to parkitmsia@gmail.com</p>
                <p>Our team will be in touch.</p>
              </div>
            </div>
          </div>
        </div>
        <div className="add-listing-message-container">
          <div className="empty-div"></div>
          <div className="add-listing-message-content">
            <h1>You have just helped one driver find a parking.</h1>
            <p>
              Congratulations. Join the ParkIt community to make parking great together!
            </p>
          </div>
        </div>
      </div>
    )
  }
}

export default ThankYou
