import { useEffect, useState } from "react";

import MainLayout from "../layouts/MainLayout";

import {
  Folder,
  FileText,
  Trash2,
  FolderPlus,
  FilePlus,
  RefreshCw,
  Pencil,
  Copy,
} from "lucide-react";
import Editor from "@monaco-editor/react";
import toast from "react-hot-toast";

import {
  getDirectories,
  getFiles,
  getFile,
  updateFile,
  getCurrentPath,
  changeDirectory,
  createDirectory,
  createFile,
  deleteFile,
  deleteDirectory,
  renameFile,
  renameDirectory,
  copyFile,
} from "../api/explorerApi";

function Explorer() {
  const [directories, setDirectories] = useState([]);

  const [files, setFiles] = useState([]);

  const [selectedFile, setSelectedFile] = useState(null);
  const [editorContent, setEditorContent] = useState("");
  const [currentPath, setCurrentPath] = useState("root");
  const [isEditing, setIsEditing] = useState(false);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const directoriesData = await getDirectories();

      const filesData = await getFiles();

      const pathData = await getCurrentPath();

      setDirectories(directoriesData);

      setFiles(filesData);

      setCurrentPath(pathData.path);
    } catch (error) {
      console.log(error);

      toast.error("Operation Failed");
    }
  };

  const handleFileClick = async (fileId) => {
    try {
      const file = await getFile(fileId);

      setSelectedFile(file);
      setEditorContent(file.content);
      setIsEditing(false);
    } catch (error) {
      console.log(error);

      toast.error("Operation Failed");
    }
  };

  const handleSave = async () => {
    try {
      await updateFile(selectedFile.id, editorContent);
      setIsEditing(false);

      toast.success("File Saved Successfully");
    } catch (error) {
      console.log(error);

      toast.error("Operation Failed");
    }
  };

  const handleDirectoryClick = async (directoryName) => {
    try {
      await changeDirectory(directoryName);

      fetchData();
    } catch (error) {
      console.log(error);

      toast.error("Operation Failed");
    }
  };

  const handleCreateFolder = async () => {
    const name = prompt("Folder Name");

    if (!name) return;

    await createDirectory(name);

    toast.success("Folder Created");

    fetchData();
  };

  const handleCreateFile = async () => {
    const name = prompt("File Name");

    if (!name) return;

    await createFile(name);

    toast.success("File Created");

    fetchData();
  };

  const handleDeleteFile = async (fileId) => {
    const confirmed = window.confirm("Delete this file?");

    if (!confirmed) return;

    await deleteFile(fileId);

    toast.success("File Deleted");

    fetchData();
  };

  const handleDeleteDirectory = async (directoryId) => {
    const confirmed = window.confirm("Delete this folder?");

    if (!confirmed) return;

    await deleteDirectory(directoryId);

    toast.success("Folder Deleted");

    fetchData();
  };

  const handleRenameFile = async (fileId, currentName) => {
    const newName = prompt("New file name", currentName);

    if (!newName) return;

    await renameFile(fileId, newName);

    fetchData();
  };

  const handleRenameDirectory = async (directoryId, currentName) => {
    const newName = prompt("New folder name", currentName);

    if (!newName) return;

    await renameDirectory(directoryId, newName);

    fetchData();
  };

  const handleCopyFile = async (fileId, currentName) => {
    const newName = prompt("Copy file as", `${currentName}_copy`);

    if (!newName) return;

    await copyFile(fileId, newName);

    fetchData();
  };

  return (
    <MainLayout>
      <h1 className="text-4xl font-bold mb-8">Explorer</h1>
      <div
        className="
    inline-flex
    items-center
    gap-2
    px-4
    py-2
    mb-6
    rounded-xl
    bg-zinc-900/60
    border
    border-zinc-800
    text-zinc-300
  "
      >
        {currentPath.split("/").map((part, index) => (
          <span key={index} className="flex items-center">
            {index > 0 && <span className="mx-2 text-zinc-500">&gt;</span>}

            <span>{part}</span>
          </span>
        ))}
      </div>
      <div className="flex flex-wrap gap-3 mb-6">
        <button
          onClick={() => handleDirectoryClick("..")}
          className="
      flex items-center gap-2
      px-4 py-2
      bg-zinc-900
      border border-zinc-800
      rounded-xl
      hover:bg-zinc-800
      transition-all
    "
        >
          ← Back
        </button>

        <button
          onClick={handleCreateFolder}
          className="
      flex items-center gap-2
      px-4 py-2
      bg-zinc-900
      border border-zinc-800
      rounded-xl
      hover:bg-zinc-800
      transition-all
    "
        >
          <FolderPlus size={18} />
          Folder
        </button>

        <button
          onClick={handleCreateFile}
          className="
      flex items-center gap-2
      px-4 py-2
      bg-zinc-900
      border border-zinc-800
      rounded-xl
      hover:bg-zinc-800
      transition-all
    "
        >
          <FilePlus size={18} />
          File
        </button>

        <button
          onClick={fetchData}
          className="
      flex items-center gap-2
      px-4 py-2
      bg-zinc-900
      border border-zinc-800
      rounded-xl
      hover:bg-zinc-800
      transition-all
    "
        >
          <RefreshCw size={18} />
          Refresh
        </button>
      </div>

      <div className="space-y-6">
        <div
          className="
    bg-zinc-900/60
    backdrop-blur-xl
    border border-zinc-800
    rounded-3xl
    p-6
    shadow-xl
  "
        >
          <div className="mb-6">
            <h2 className="text-xl font-semibold">Explorer</h2>

            <p className="text-zinc-500 text-sm">
              Browse files and directories
            </p>
          </div>
          <div className="space-y-2">
            <h3 className="text-zinc-400 text-xs uppercase tracking-widest mb-3">
              Folders
            </h3>

            {directories.length === 0 && (
              <p className="text-zinc-500 text-sm">No folders</p>
            )}
            {directories.map((directory) => (
              <div
                key={directory.id}
                className={`
  flex
    items-center
    justify-between
    p-4
    rounded-2xl
    border
    transition-all
    duration-200
  ${
    currentPath.includes(directory.name)
      ? "bg-blue-500/10 border-blue-500/40"
      : "bg-zinc-900/30 border-zinc-800 hover:bg-zinc-800/40 hover:border-zinc-700"
  }
`}
              >
                <div
                  onClick={() => handleDirectoryClick(directory.name)}
                  className="flex items-center gap-4 cursor-pointer"
                >
                  <Folder size={24} className="text-blue-400" />

                  <div>
                    <p className="font-semibold">{directory.name}</p>

                    <p className="text-xs text-zinc-500">Folder</p>
                  </div>
                </div>

                <div className="flex items-center gap-3">
                  <button
                    onClick={() =>
                      handleRenameDirectory(directory.id, directory.name)
                    }
                    className="
      text-zinc-500
      hover:text-blue-400
      transition-colors
    "
                  >
                    <Pencil
                      size={18}
                      className="
    text-zinc-500
    hover:text-blue-400
    transition-colors
  "
                    />
                  </button>

                  <button onClick={() => handleDeleteDirectory(directory.id)}>
                    <Trash2
                      size={18}
                      className="
        text-zinc-500
        hover:text-red-400
        transition-colors
      "
                    />
                  </button>
                </div>
              </div>
            ))}

            <div className="border-t border-zinc-800 my-4"></div>

            <h3 className="text-zinc-400 text-xs uppercase tracking-widest mb-3">
              Files
            </h3>

            {files.length === 0 && (
              <p className="text-zinc-500 text-sm">No files</p>
            )}

            {files.map((file) => (
              <div
                key={file.id}
                className={`
  flex
    items-center
    justify-between
    p-4
    rounded-2xl
    border
    transition-all
  ${
    selectedFile?.id === file.id
      ? "bg-blue-500/10 border-blue-500/40"
      : "bg-zinc-900/30 border-zinc-800 hover:bg-zinc-800/40"
  }
`}
              >
                <div
                  onClick={() => handleFileClick(file.id)}
                  className="flex items-center gap-4 cursor-pointer"
                >
                  <FileText size={24} className="text-green-400" />

                  <div>
                    <p className="font-semibold">{file.name}</p>

                    <p className="text-xs text-zinc-500">
                      Text File • {file.permission}
                    </p>
                  </div>
                </div>

                <div className="flex items-center gap-3">
                  <button onClick={() => handleRenameFile(file.id, file.name)}>
                    <Pencil
                      size={18}
                      className="
      text-zinc-500
      hover:text-blue-400
      transition-colors
    "
                    />
                  </button>

                  <button onClick={() => handleCopyFile(file.id, file.name)}>
                    <Copy
                      size={18}
                      className="
      text-zinc-500
      hover:text-green-400
      transition-colors
    "
                    />
                  </button>

                  <button onClick={() => handleDeleteFile(file.id)}>
                    <Trash2
                      size={18}
                      className="
        text-zinc-500
        hover:text-red-400
        transition-colors
      "
                    />
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div
          className="
    bg-zinc-900/60
    backdrop-blur-xl
    border border-zinc-800
    rounded-3xl
    p-6
    shadow-xl
  "
        >
          {selectedFile ? (
            <>
              <div className="flex items-center justify-between mb-4">
                <div>
                  <h2 className="text-2xl font-bold">{selectedFile.name}</h2>

                  <p className="text-zinc-500 text-sm mt-1">
                    {selectedFile.permission}
                  </p>
                </div>

                <div className="flex gap-3">
                  {!isEditing ? (
                    <button
                      onClick={() => setIsEditing(true)}
                      className="
        px-5
        py-2
        bg-blue-500
        text-white
        rounded-xl
        font-semibold
        hover:bg-blue-600
      "
                    >
                      Edit
                    </button>
                  ) : (
                    <button
                      onClick={handleSave}
                      className="
        px-5
        py-2
        bg-white
        text-black
        rounded-xl
        font-semibold
        hover:opacity-90
      "
                    >
                      Save
                    </button>
                  )}
                </div>
              </div>
              <Editor
                height="600px"
                theme="vs-dark"
                defaultLanguage="plaintext"
                value={editorContent}
                onChange={(value) => setEditorContent(value || "")}
                options={{
                  minimap: {
                    enabled: false,
                  },
                  fontSize: 14,
                  wordWrap: "on",
                  automaticLayout: true,
                  readOnly: !isEditing,
                }}
              />
            </>
          ) : (
            <div className="flex flex-col items-center justify-center h-full text-zinc-500">
              <FileText size={60} />

              <p className="mt-4 text-lg">Select a file to start editing</p>
            </div>
          )}
        </div>
      </div>
    </MainLayout>
  );
}

export default Explorer;
