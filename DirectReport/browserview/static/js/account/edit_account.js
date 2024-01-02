const { useState, useEffect } = React;
const EditAccountForm = () => {
    return (
        <form className="space-y-4 md:space-y-6" method="POST" action="/signup">
            <div>
                <label htmlFor="email" className="block mb-2 text-sm font-medium text-white dark:text-white">Your email</label>
                <input type="email" name="email" id="email" className="bg-gray-50 border border-gray-300 text-blue-500 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@company.com" required=""/>
            </div>
            <div>
                <label htmlFor="firstname" className="block mb-2 text-sm font-medium text-white dark:text-white">
                    First name
                </label>
                <input type="firstname" name="firstname" id="firstname" className="bg-gray-50 border border-gray-300 text-blue-500 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="John Doe.." required=""/>
            </div>
            <div>
                <label htmlFor="lastname" className="block mb-2 text-sm font-medium text-white dark:text-white">
                    Last name
                </label>
                <input type="text" name="lastname" id="lastname" className="bg-gray-50 border border-gray-300 text-blue-500 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="John Doe.." required=""/>
            </div>
            <div>
                <label htmlFor="username" className="block mb-2 text-sm font-medium text-white dark:text-white">
                    Username
                </label>
                <input type="text" name="username" id="username" className="bg-gray-50 border border-gray-300 text-blue-500 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="John Doe.." required=""/>
            </div>
            <div>
                <label htmlFor="password" className="block mb-2 text-sm font-medium text-white dark:text-white">Password</label>
                <input type="password" name="password" id="password" placeholder="••••••••" className="bg-gray-50 border border-gray-300 text-blue-500 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required=""/>
            </div>
            <button type="submit" className="w-full text-white bg-sky-500 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-3xl text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
                Update Account
            </button>
        </form>
    )
}

const EditAccount = () => {
    return (
        <div>
            <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
                <div className="w-full bg-blue-500 rounded-3xl shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
                    <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
                        <h1 className="text-xl font-bold leading-tight tracking-tight text-white md:text-2xl dark:text-white">
                            Edit Account
                        </h1>
                        {EditAccountForm()}
                    </div>
                </div>
            </div>
        </div>
    )
}

const domContainer = document.querySelector('#root');
ReactDOM.render(<EditAccount/>, domContainer);