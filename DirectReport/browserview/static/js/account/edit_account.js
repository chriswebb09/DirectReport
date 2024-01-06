const { useState, useEffect } = React;

const EditAccount = () => {
    return (
        <div>
            <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
                <div className="w-full bg-blue-500 rounded-3xl shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
                    <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
                        <h1 className="text-xl font-bold leading-tight tracking-tight text-white md:text-2xl dark:text-white">
                            Edit Account
                        </h1>
                        {AccountForm("/edit", "Update Account")}
                    </div>
                </div>
            </div>
        </div>
    )
}

const domContainer = document.querySelector('#root');
ReactDOM.render(<EditAccount/>, domContainer);