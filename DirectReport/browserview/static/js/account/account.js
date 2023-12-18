
const { useState, useEffect } = React;

const Account = () => {
    const [userData, setUserData] = useState({});
    const [actualData, setActualData] = useState({});
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
            .then((actualData) => {
                setUserData(actualData["user"]);
                setReportData(actualData["reports"]);
                setActualData(actualData);
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
            <div className="mx-30 content-center mt-0 mb-48 h-150">
                <div className="pt-5 pb-3 mt-0 mb-5 ml-20 px-20">
                    <h1 className="text-2xl text-blue-800 text-left font-bold font-mono pt-5">
                        User Account
                    </h1>
                </div>

                <div className="grid grid-cols-3 gap-8 mb-1 mx-20 px-20 justify-center">
                    {userData && AccountUserInfo(userData, reportData)}
                </div>
            </div>
        )
    }
};



const domContainer = document.querySelector('#root');
ReactDOM.render(<Account/>, domContainer);