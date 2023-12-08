
const { useState, useEffect } = React;
const Account = () => {

    const [userData, setUserData] = useState({});
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch(`/account_data`)
            .then((response) => {
                if (!response.ok) {
                    throw new Error(
                        `This is an HTTP error: The status is ${response.status}`
                    );
                }
                return response.json();
            })
            .then((actualData) => {
                setUserData(actualData)
                setError(null);
            })
            .catch((err) => {
                setError(err.message);
                setUserData(null)

            })
            .finally(() => {
                setLoading(false);
            });
    }, []);


    if (loading) {
        return (
            <div>{`There is a problem fetching the post data - ${error}`}</div>
        )
    } else {
        return (
            <div className="grid grid-cols-3 gap-1 mb-20 mx-10">
                <div className="col-span-1 justify-center my-10">
                    <div className="self-center bg-blue-200 py-10 px-10 my-5 shadow-lg rounded-2xl">
                        <h1 className="text-center py-10 bg-blue-50 rounded-2xl">Account: {userData.name}</h1>
                        <a className="px-6 text-md hover:text-gray-200" href="/teamreport">
                            <button type="button"
                                    className="w-full text-white bg-indigo-700 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Reports
                            </button>
                        </a>
                        <p className="text-center">{userData.userid} content</p>
                    </div>
                </div>
                <div className="col-span-1 justify-center my-10">
                    <div className="self-center bg-blue-200 py-10 py-10 px-10 my-5 shadow-lg rounded-2xl">
                        <h1 className="text-center py-10 bg-blue-50 rounded-2xl">Account: {userData.userid}</h1>
                        <form method="GET" action="/logout">
                            <button className="button is-block is-info is-large is-fullwidth">Logout</button>
                        </form>
                    </div>
                </div>
                <div className="col-span-1 justify-center my-10">
                    <div className="self-center bg-blue-200 py-10 px-10 my-5 shadow-lg rounded-2xl">
                        <h1 className="text-center py-10 bg-blue-50 rounded-2xl">Account: {userData.userid}</h1>
                        <p className="text-center">{userData.userid} content</p>
                    </div>
                </div>
                <div className="col-span-3 justify-center my-10">
                    <div className="self-center bg-blue-200 py-10 px-10 my-5 shadow-lg rounded-2xl">
                        <h1 className="text-center py-10 bg-blue-50 rounded-2xl">Account: {userData.userid}</h1>
                        <p className="text-center">{userData.userid} content</p>
                    </div>
                </div>
            </div>
        )
    }
};
const domContainer = document.querySelector('#root');
ReactDOM.render(<Account/>, domContainer);

// class Account extends React.Component {
//     render() {
//         return elem(
//             'div',
//             null,
//             React.createElement(
//                 'div',
//                 {
//                     className: "py-24 flex h-100",
//                     style: {background: "linear-gradient(90deg, #667eea 0%, #764ba2 100%)"}
//                 },
//                 React.createElement(
//                     "div",
//                     {
//                         className: "container mx-auto px-6"
//                     },
//                     React.createElement(
//                         "h2",
//                         {
//                             className: "my-4 text-4xl font-bold mb-2 text-white"
//                         },
//                         "DirectReport."
//                     ),
//                     React.createElement(
//                         "h3",
//                         {
//                             className: "my-8 text-2xl mb-12 text-gray-200"
//                         },
//                         "Keep track of your accomplishments each day of the workweek."
//                     ),
//                     React.createElement(
//                         "div",
//                         {
//                             className: "my-8"
//                         },
//                         React.createElement(
//                             "a",
//                             {
//                                 className: "my-12 px-14 py-5 text-lg font-bold text-center text-white bg-gray-400 rounded-full hover:bg-blue-800 shadow-lg uppercase",
//                                 href: "https://github.com/chriswebb09/DirectReport"
//                             },
//                             "Github"
//                         )
//                     )
//                 )
//             )
//         );
//     }
// }
//
// const domContainer = document.querySelector('#root');
// ReactDOM.render(elem(Home), domContainer);