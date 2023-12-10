
const { useState, useEffect } = React;
const TeamMember = () => {

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
            <div className="grid grid-cols-3 gap-8 mb-1 mx-20 justify-cente">
                <div className="lg:col-span-1 md: col-span-1 sm:col-span-3 justify-center my-1">
                    <div className="self-center bg-blue-200 py-10 px-10 my-2 shadow-lg rounded-2xl">
                        <h1 className="text-center py-10 mb-10 bg-blue-50 rounded-2xl">Account: {userData.name}</h1>
                        <p className="text-center">{userData.userid} content</p>
                    </div>
                </div>
                <div className="lg:col-span-1 sm:col-span-3 justify-center my-1">
                    <div className="self-center bg-blue-200 py-10 py-10 px-10 my-2 shadow-lg rounded-2xl">
                        <h1 className="text-center mb-10 py-10 bg-blue-50 rounded-2xl">Account: {userData.userid}</h1>
                        <a className="py-10 text-md hover:text-gray-200" href="/teamreport">
                            <button type="button" className="w-full text-white bg-indigo-700 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Reports
                            </button>
                        </a>
                    </div>
                </div>
                <div className="lg:col-span-1 sm:col-span-3 justify-center my-1">
                    <div className="self-center bg-blue-200 py-10 px-10 my-2 shadow-lg rounded-2xl">
                        <h1 className="text-center py-10 mb-10 bg-blue-50 rounded-2xl">Account: {userData.userid}</h1>
                        <p className="text-center">{userData.userid} content</p>
                    </div>
                </div>
                <div className="col-span-3 justify-center my-1">
                    <div className="self-center bg-blue-200 py-10 px-10 my-2 shadow-lg rounded-2xl">
                        <div className="mx-80">
                            <a className="px-6 text-md hover:text-gray-200" href="/logout">
                                <button type="button" className="w-full text-white bg-indigo-700 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
                                    Log Out
                                </button>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
};

const domContainer = document.querySelector('#root');
ReactDOM.render(<TeamMember/>, domContainer);