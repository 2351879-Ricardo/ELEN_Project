const serverHref = "http://127.0.0.1:5000";

function FetchServer(input, path) {
  return new Promise((resolve) => {
    fetch(serverHref + path, {
      method: "POST",
      headers: {
        "Content-type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify(input),
    })
      .then((resposne) => {
        return resposne.json();
      })
      .then((json) => {
        resolve(json);
      });
  });
}

function GetServer(path) {
  return new Promise((resolve) => {
    fetch(serverHref + path, {
      method: "GET",
    })
      .then((resposne) => {
        return resposne.json();
      })
      .then((json) => {
        resolve(json);
      });
  });
}

function FetchUserExists(userId) {
  return new Promise((resolve) => {
    fetch(serverHref + "/signup/exists", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify(userId),
    })
      .then((resposne) => {
        return resposne.json();
      })
      .then((json) => {
        resolve(json);
      });
  });
}

function PostNewUser(username, pword) {
  return new Promise((resolve) => {
    let userDetails = { userID: username, password: pword };
    fetch(serverHref + "/signup/create", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify(userDetails),
    })
      .then((resposne) => {
        return resposne.json();
      })
      .then((json) => {
        resolve(json);
      });
  });
}

function FetchValidSignIn(username, pword) {
  return new Promise((resolve) => {
    let userDetails = { userID: username, password: pword };
    fetch(serverHref + "/signin/valid", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify(userDetails),
    })
      .then((resposne) => {
        return resposne.json();
      })
      .then((json) => {
        resolve(json);
      });
  });
}

// Dates
function GetFirstUserEntry() {
  return "2021-12-29";
}
function GetToday() {
  let today = new Date();
  let day = ("0" + today.getDate()).slice(-2);
  let month = ("0" + (today.getMonth() + 1)).slice(-2);
  let year = today.getFullYear();
  return year + "-" + month + "-" + day;
}
