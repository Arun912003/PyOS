import {
  LayoutDashboard,
  FolderOpen,
  Search,
  History,
  Trash2,
  FileText,
  User,
  Terminal,
} from "lucide-react";

import { useEffect, useState } from "react";
import { getProfile } from "../api/userApi";

import { NavLink, useNavigate } from "react-router-dom";

function MainLayout({ children }) {
  const navigate = useNavigate();

  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const data = await getProfile();

        setUser(data);
      } catch (error) {
        console.log(error);
      }
    };

    fetchProfile();
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");

    navigate("/");
  };

  const navClass = ({ isActive }) =>
    `flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200 ${
      isActive
        ? "bg-gradient-to-r from-blue-500 to-cyan-400 text-white font-semibold shadow-lg shadow-blue-500/20"
        : "text-zinc-400 hover:bg-zinc-800 hover:text-white"
    }`;

  return (
    <div className="h-screen bg-gradient-to-br from-zinc-950 via-slate-950 to-blue-950 text-white flex overflow-hidden">
      <aside
        className="
w-72
h-screen
border-r
border-zinc-800/50
bg-zinc-950/50
backdrop-blur-2xl
p-6
flex
flex-col
shrink-0
shadow-2xl
"
      >
        <div className="flex items-center gap-4 mb-12">
          <div
            className="
      p-3
      rounded-2xl
      bg-gradient-to-br
      from-blue-500
      via-cyan-500
      to-blue-600
      shadow-lg
      shadow-blue-500/20
    "
          >
            <Terminal size={24} />
          </div>

          <div>
            <h1
              className="
        text-3xl
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
      "
            >
              Virtual File System
            </p>
          </div>
        </div>

        <nav className="flex flex-col gap-2">
          <NavLink to="/dashboard" className={navClass}>
            <LayoutDashboard size={20} />
            Dashboard
          </NavLink>

          <NavLink to="/explorer" className={navClass}>
            <FolderOpen size={20} />
            Explorer
          </NavLink>

          <NavLink to="/search" className={navClass}>
            <Search size={20} />
            Search
          </NavLink>

          <NavLink to="/history" className={navClass}>
            <History size={20} />
            History
          </NavLink>

          <NavLink to="/logs" className={navClass}>
            <FileText size={20} />
            Logs
          </NavLink>

          <NavLink to="/recycle-bin" className={navClass}>
            <Trash2 size={20} />
            Recycle Bin
          </NavLink>
        </nav>

        <div className="mt-auto pt-6">
          <div
            className="
      flex
      items-center
      gap-3
      px-4
      py-3
      mb-2
      text-zinc-300
    "
          >
            <User size={18} />

            <span className="font-medium">
              {user?.username
                ? user.username.charAt(0).toUpperCase() + user.username.slice(1)
                : "User"}
            </span>
          </div>

          <button
            onClick={handleLogout}
            className="
      w-full
      flex
      items-center
      gap-3
      px-4
      py-3
      rounded-xl
      text-red-400
      hover:bg-red-950
      transition-all
    "
          >
            🚪 Logout
          </button>
        </div>
      </aside>

      <main className="flex-1 h-screen overflow-y-auto p-10 relative">
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
        {children}
      </main>
    </div>
  );
}

export default MainLayout;
