import { useEffect, useState } from "react";

import MainLayout from "../layouts/MainLayout";

import { getDiskInfo } from "../api/filesystemApi";

import {
  FolderOpen,
  FileText,
  Trash2
} from "lucide-react";

function Dashboard() {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      console.log("ACCESS TOKEN:", localStorage.getItem("access"));

      const data = await getDiskInfo();

      console.log("DISK INFO:", data);

      setStats(data);
    } catch (error) {
      console.log("ERROR:", error);
    }
  };

  return (
    <MainLayout>
      <div className="mb-10">
        <h1 className="text-5xl font-bold">Dashboard</h1>

        <p className="text-zinc-400 mt-2">
          Manage your files, folders and system activity.
        </p>
      </div>

      <div className="grid md:grid-cols-3 gap-6">
        <div
          className="
      bg-zinc-900/60
      backdrop-blur-xl
      border border-zinc-800
      rounded-3xl
      p-8
      hover:border-blue-500
      hover:-translate-y-1
      transition-all
      duration-300
      shadow-xl
    "
        >
          <FolderOpen size={30} className="text-blue-400" />

          <p className="text-zinc-400 mt-4">Directories</p>

          <h2 className="text-5xl font-bold mt-2">{stats?.directories ?? 0}</h2>
        </div>

        <div
          className="
      bg-zinc-900/60
      backdrop-blur-xl
      border border-zinc-800
      rounded-3xl
      p-8
      hover:border-green-500
      hover:-translate-y-1
      transition-all
      duration-300
      shadow-xl
    "
        >
          <FileText size={30} className="text-green-400" />

          <p className="text-zinc-400 mt-4">Files</p>

          <h2 className="text-5xl font-bold mt-2">{stats?.files ?? 0}</h2>
        </div>

        <div
          className="
      bg-zinc-900/60
      backdrop-blur-xl
      border border-zinc-800
      rounded-3xl
      p-8
      hover:border-red-500
      hover:-translate-y-1
      transition-all
      duration-300
      shadow-xl
    "
        >
          <Trash2 size={30} className="text-red-400" />

          <p className="text-zinc-400 mt-4">Recycle Bin</p>

          <h2 className="text-5xl font-bold mt-2">{stats?.recycle_bin ?? 0}</h2>
        </div>
      </div>
    </MainLayout>
  );
}

export default Dashboard;
