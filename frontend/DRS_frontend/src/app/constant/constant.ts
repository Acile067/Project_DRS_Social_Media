export const Constant = {
  API_METHOD: {
    GET_ALL_USERS: 'user/users',
    REGISTER_USER: 'user/register',
    LOGIN_USER: 'user/login',
    EDIT_PROFILE: 'user/edituserprofile',
    CREATE_POST: 'post/createpost',
    UNAPPROVED_POSTS: 'post/unapproved',
    APPROVE_POST: 'post/approve',
    REJECT_POST: 'post/reject',
    APPROVED_POSTS_FOR_USER: 'post/approvedpostsforuser',
    SEARCH_FRIEND: 'user/searchfriend',
    ADD_FRIEND: 'relationships/addfriend',
    GET_FRIEND_REQUESTS: 'relationships/friendrequests',
    RESPONDE_FRIEND_REQUEST: 'relationships/respondfriend',
    GET_MY_FRIENDS: 'relationships/friends',
    DELETE_FRIEND: 'relationships/deleterelationship',
  },
  ALERT_MESSAGES: {
    UNKONOW_ERROR: 'An unknown error occurred',
    UNKNOWN_RESPONSE: 'Unknown response',
  },
  LOCAL_STORAGE_TOKEN: 'token',
};
