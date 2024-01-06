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

const NameElement = (type, forHtml, labelText, name, id, placeholder, value) => {
    return (
        <div>
            <label htmlFor={forHtml} className="block mb-2 text-sm font-semibold tracking-wider text-white dark:text-white">
                {labelText}
            </label>
            <input type={type} name={name} id={id} className="bg-gray-50 border border-gray-300 text-blue-500 tracking-wider sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 font-semibold" placeholder={placeholder} required="" value={value}/>
        </div>
    )
}

const AccountForm = (action, submit_button) => {
    return (
        <form className="space-y-4 md:space-y-6" method="POST" action={action}>
            {NameElement("email", "email", "Your email", "email", "email", "name@company.com", "name@company.com")}
            {NameElement("text", "firstname", "First name", "firstname", "firstname", "John", "John")}
            {NameElement("text", "lastname", "Last name", "lastname", "lastname", "Doe", "Doe")}
            {NameElement("text", "username", "Username", "username", "username", "JohnDoe", "JohnDoe")}
            {NameElement("password", "password", "Password", "password", "password", "••••••••", "••••••••")}
            <div className="flex items-center justify-between">
                {RememberMe()}
            </div>
            <button type="submit" className="w-full text-white bg-sky-500 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-3xl text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
                {submit_button}
            </button>
        </form>
    )
}
