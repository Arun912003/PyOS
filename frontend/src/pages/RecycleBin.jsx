import { useEffect, useState } from "react";

import MainLayout from "../layouts/MainLayout";

import {
  getRecycleBin,
  restoreFile,
  emptyRecycleBin
} from "../api/recycleBinApi";

function RecycleBin() {

  const [files, setFiles] =
    useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {

    const data =
      await getRecycleBin();

    setFiles(data);
  };

  const handleRestore =
    async (id) => {

      await restoreFile(id);

      fetchData();
    };

  const handleEmpty =
    async () => {

      const confirmed =
        window.confirm(
          "Empty Recycle Bin?"
        );

      if (!confirmed) return;

      await emptyRecycleBin();

      fetchData();
    };

  return (
    <MainLayout>

      <div className="flex justify-between items-center mb-8">

        <h1 className="text-4xl font-bold">
          Recycle Bin
        </h1>

        <button
          onClick={handleEmpty}
          className="px-4 py-2 bg-red-600 rounded-lg"
        >
          Empty Bin
        </button>

      </div>

      <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-6">

        {files.length === 0 ? (
          <p className="text-zinc-500">
            Recycle Bin Empty
          </p>
        ) : (
          files.map((file) => (

            <div
              key={file.id}
              className="flex justify-between items-center p-3 border-b border-zinc-800"
            >

              <div>

                <p>
                  {file.file_name}
                </p>

                <p className="text-sm text-zinc-500">
                  {file.deleted_at}
                </p>

              </div>

              <button
                onClick={() =>
                  handleRestore(
                    file.id
                  )
                }
                className="px-4 py-2 bg-green-600 rounded-lg"
              >
                Restore
              </button>

            </div>

          ))
        )}

      </div>

    </MainLayout>
  );
}

export default RecycleBin;