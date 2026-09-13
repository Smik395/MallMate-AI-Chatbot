const input = document.getElementById("messageInput");

const sendButton =
    document.getElementById("sendButton");

const chatMessages =
    document.getElementById("chatMessages");


// SEND MESSAGE

async function sendMessage() {

    const message = input.value.trim();

    if (message === "") {
        return;
    }


    // Show user message

    addMessage(
        message,
        "user"
    );


    input.value = "";


    // Send message to Python

    try {

        const response = await fetch(
            "/chat",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    message: message
                })
            }
        );


        const data =
            await response.json();


        // Show bot response

        addMessage(
            data.response,
            "bot"
        );


    } catch (error) {

        addMessage(
            "Sorry, something went wrong.",
            "bot"
        );

        console.error(error);

    }

}


// ADD MESSAGE TO CHAT

function addMessage(
    text,
    type
) {

    const message =
        document.createElement("div");


    message.classList.add(
        "message"
    );


    if (type === "user") {

        message.classList.add(
            "user-message"
        );

    } else {

        message.classList.add(
            "bot-message"
        );

    }


    message.innerText = text;


    chatMessages.appendChild(
        message
    );


    chatMessages.scrollTop =
        chatMessages.scrollHeight;

}


// QUICK SUGGESTION

function sendSuggestion(
    text
) {

    input.value = text;

    sendMessage();

}


// ENTER KEY

input.addEventListener(
    "keydown",
    function(event) {

        if (event.key === "Enter") {

            sendMessage();

        }

    }
);