window.indexedDB = window.indexedDB;

if (!window.indexedDB)
{
    alert("No Database Available");
}

let request = window.indexedDB.open("User_Logins"), db, tx, store, index;

request.onerror = function (e) 
{
    console.log("An Error Occured: " + e.target.errorCode);
}

request.onupgradeneeded = function (e)
{
    console.log("Upgrade Required: " + e);
    let db = request.result, store = db.createObjectStore("UsersStore", {autoIncrement: true}), index = store.createIndex("user");
}

request.onsuccess = function (e)
{
    console.log("Success");
    db = request.result;
}

