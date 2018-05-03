import {SET_AUTHED_USER} from "../actions/AuthedUser"

export default function users(state = null, action) {
  switch (action.type) {
    case SET_AUTHED_USER :
      return action.id
    default :
      return state
  }
}
