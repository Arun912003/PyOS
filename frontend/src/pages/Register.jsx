import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { registerUser } from "../api/authApi";
import { Terminal } from "lucide-react";
import toast from "react-hot-toast";

function Register() {
  const navigate = useNavigate();

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();

    if (password !== confirmPassword) {
      toast.error("Passwords do not match");

      return;
    }

    try {
      await registerUser(username, email, password);

      toast.success("Registration Successful");

      navigate("/");
    } catch (error) {
      console.log(error);

      toast.error("Registration Failed");
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-zinc-950 via-slate-950 to-blue-950 flex items-center justify-center px-4 relative overflow-hidden">
      <div
        className="
        absolute
        top-0
        right-0
        w-[500px]
        h-[500px]
        bg-blue-500/10
        blur-3xl
        rounded-full
        pointer-events-none
      "
      />

      <div
        className="
        absolute
        bottom-0
        left-0
        w-[400px]
        h-[400px]
        bg-purple-500/10
        blur-3xl
        rounded-full
        pointer-events-none
      "
      />
      <div className="w-full max-w-md bg-zinc-900/80 backdrop-blur-xl border border-zinc-800 rounded-3xl p-8 shadow-2xl">
        <div className="flex flex-col items-center mb-6">
          <div
            className="
      p-4
      rounded-2xl
      bg-gradient-to-br
      from-blue-500
      via-cyan-500
      to-blue-600
      shadow-lg
      shadow-blue-500/20
      mb-4
    "
          >
            <Terminal size={28} />
          </div>

          <h1
            className="
      text-4xl
      font-black
      tracking-tight
      bg-gradient-to-r
      from-blue-400
      via-cyan-300
      to-white
      bg-clip-text
      text-transparent
    "
          >
            PyOS
          </h1>

          <p
            className="
      text-xs
      uppercase
      tracking-widest
      text-zinc-500
      mt-2
    "
          >
            Create Your Account
          </p>
        </div>

        <form onSubmit={handleRegister} className="mt-8 space-y-4">
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="
              w-full
              bg-zinc-800/80
              border border-zinc-700
              rounded-xl
              px-4 py-3
              text-white
              outline-none
              focus:border-blue-500
              transition-all
            "
          />

          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="
              w-full
              bg-zinc-800/80
              border border-zinc-700
              rounded-xl
              px-4 py-3
              text-white
              outline-none
              focus:border-blue-500
              transition-all
            "
          />

          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="
              w-full
              bg-zinc-800/80
              border border-zinc-700
              rounded-xl
              px-4 py-3
              text-white
              outline-none
              focus:border-blue-500
              transition-all
            "
          />

          <input
            type="password"
            placeholder="Confirm Password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            className="
              w-full
              bg-zinc-800/80
              border border-zinc-700
              rounded-xl
              px-4 py-3
              text-white
              outline-none
              focus:border-blue-500
              transition-all
            "
          />

          <button
            type="submit"
            className="
              w-full
              bg-blue-500
              hover:bg-blue-600
              text-white
              py-3
              rounded-xl
              font-semibold
              transition-all
            "
          >
            Create Account
          </button>
        </form>

        <p className="text-center mt-6 text-zinc-400">
          Already have an account?
          <Link to="/" className="ml-2 text-blue-400 hover:text-blue-300">
            Login
          </Link>
        </p>
      </div>
    </div>
  );
}

export default Register;
