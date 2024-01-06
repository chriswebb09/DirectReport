const { useState, useEffect } = React;

const domContainer = document.querySelector('#root');

ReactDOM.render(<UserAccount action="/signup" header="Sign up for an account" button_title="Create Account"/>, domContainer);