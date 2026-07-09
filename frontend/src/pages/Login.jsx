import Navbar from "../components/Navbar";

const Login = () => {
  return (
    <>
      <Navbar />

      <div className="min-h-screen flex items-center justify-center">
        <div className="w-full max-w-md border rounded-lg shadow p-8">

          <h1 className="text-3xl font-bold text-center mb-6">
            Login
          </h1>

          <form className="space-y-4">

            <div>
              <label className="block mb-2">
                Email
              </label>

              <input
                type="email"
                placeholder="Enter your email"
                className="w-full border rounded px-4 py-2"
              />
            </div>

            <div>
              <label className="block mb-2">
                Password
              </label>

              <input
                type="password"
                placeholder="Enter your password"
                className="w-full border rounded px-4 py-2"
              />
            </div>

            <button
              type="submit"
              className="w-full bg-blue-600 text-white py-2 rounded"
            >
              Login
            </button>

          </form>

        </div>
      </div>
    </>
  );
};

export default Login;