const serverHref = "http://127.0.0.1:5000";

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
        console.log(json);
        resolve(json);
        //return json;
      });
  });
}

function PostNewUser(username, pword) {
  return new Promise((resolve) => {
    let userDetails = { userId: username, password: pword };
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
        console.log(json);
        return json;
      });
  });
}
