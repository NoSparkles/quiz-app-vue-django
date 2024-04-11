<template>
    <div class="yes-no-modal-wrapper" @click.self="$emit('close')">
        <div class="yes-no-modal">
            <h1>{{ question }}</h1>
            <div>
                <button class='yes-button' @click="$emit('yes')">{{ yesText }}</button>
                <button class='no-button' @click="$emit('no')">{{ noText }}</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: [
        'question',
        'yesText',
        'noText'
    ],
    setup() {

        return {

        }
    }
}
</script>

<style>
.yes-no-modal-wrapper {
    width: 100%;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.5);
    position: fixed;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    z-index: 999;
}

.yes-no-modal-wrapper .yes-no-modal {
    background-color: white;
    opacity: 1;
    padding: 40px 40px;
    display: flex;
    max-width: 80%;
    flex-direction: column;
    border-radius: 20px;
}

.yes-no-modal-wrapper .yes-no-modal h1 {
    align-self: center;
    text-align: center;
    max-width: 80%;
    text-wrap: wrap;
}

.yes-no-modal-wrapper .yes-no-modal div {
    display: flex;
    justify-content: center;
    gap: 20px
}

.yes-no-modal-wrapper .yes-no-modal div button {
    cursor: pointer;
    color: white;
    background-color: #555;
    padding: 8px 40px;
    font-size: 1.4em;
    width: fit-content;
    align-self: center;
    border: none;
    margin-top: 20px;
    border-radius: 8px;
}

.yes-no-modal-wrapper .yes-no-modal .yes-button {
    background-color: rgb(18, 255, 97);
    font-weight: bold;
}

.yes-no-modal-wrapper .yes-no-modal .no-button {
    background-color: rgb(255, 84, 61);
    font-weight: bold;
}
</style>