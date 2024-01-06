const { useState, useEffect } = React;

const domContainer = document.querySelector('#root');
ReactDOM.render(<UserAccount action="/edit" header="Edit Account" button_title="Update Account"/>, domContainer);