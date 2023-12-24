
const { useState, useEffect } = React;

const Account = () => {
    const [userData, setUserData] = useState({});
    const [reportData, setReportData] = useState([]);
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
            .then((responseData) => {
                setUserData(responseData["user"]);
                setReportData(responseData["reports"]);
                setError(null);
            })
            .catch((err) => {
                setUserData(null)
                setReportData(null)
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
            <div className="mx-20 content-center mt-0 mb-0 h-50">
                <div className="grid grid-cols-3 gap-8 mx-10 px-10 mt-2 justify-center">
                    {userData && AccountUserInfo(userData, reportData)}
                </div>
            </div>
        )
    }
};



const domContainer = document.querySelector('#root');
ReactDOM.render(<Account/>, domContainer);