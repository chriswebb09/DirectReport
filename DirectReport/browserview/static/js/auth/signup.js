const { useState, useEffect } = React;


const RememberMe = () => {
    return (
        <div className="flex items-start">
            <div className="flex items-center h-5">
                <input id="remember" name="remember" aria-describedby="remember" type="checkbox" className="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800" required=""/>
            </div>
            <div className="ml-3 text-sm">
                <label htmlFor="remember" className="text-white dark:text-gray-300">
                    Remember me
                </label>
            </div>
        </div>
    )
}

const NameElement = (forHtml, labelText, name, id, placeholder) => {
    return (
        <div>
            <label htmlFor={forHtml} className="block mb-2 text-sm font-semibold tracking-wider text-white dark:text-white">
                {labelText}
            </label>
            <input type="text" name={name} id={id} className="bg-gray-50 border border-gray-300 text-blue-500 tracking-wider sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 font-semibold" placeholder={placeholder} required=""/>
        </div>
    )
}

const AccountForm = (action, submit_button) => {
    return (
        <form className="space-y-4 md:space-y-6" method="POST" action={action}>
            <div>
                <label htmlFor="email" className="block mb-2 text-sm font-semibold tracking-wider  text-white dark:text-white">
                    Your email
                </label>
                <input type="email" name="email" id="email" className="bg-gray-50 border border-gray-300 text-blue-500 tracking-wider sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 font-semibold" placeholder="name@company.com" required=""/>
            </div>
            {NameElement("firstname", "First name", "firstname", "firstname", "John")}
            {NameElement("lastname", "Last name", "lastname", "lastname", "Doe")}
            {NameElement("username", "Username", "username", "username", "JohnDoe")}
            <div>
                <label htmlFor="password" className="block mb-2 text-sm font-medium tracking-wider text-white dark:text-white">Password</label>
                <input type="password" name="password" id="password" placeholder="••••••••" className="bg-gray-50 border border-gray-300 text-blue-500 font-semibold tracking-wider sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required=""/>
            </div>
            <div className="flex items-center justify-between">
                {RememberMe()}
            </div>
            <button type="submit" className="w-full text-white bg-sky-500 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-3xl text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
                {submit_button}
            </button>
        </form>
    )
}

const Signup = () => {
    return (
        <div>
            <div className="flex flex-col items-center justify-center mx-auto py-10">
                <div className="w-full bg-blue-500 rounded-3xl shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
                    <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
                        <h1 className="text-xl font-bold leading-tight tracking-tight text-white md:text-2xl dark:text-white">
                            Sign up for an account
                        </h1>
                        {AccountForm("/signup", "Create Account")}
                    </div>
                </div>
            </div>
        </div>
    )
}

const domContainer = document.querySelector('#root');
ReactDOM.render(<Signup/>, domContainer);