<template>
    <div class="yes-no-modal-wrapper" @click.self="$emit('close')">
        <div ref="el" class="yes-no-modal">
            <h1>{{ question }}</h1>
            <div>
                <button class='yes-button' @click="handleYes">{{ yesText }}</button>
                <button class='no-button' @click="handleNo">{{ noText }}</button>
            </div>
        </div>
    </div>
</template>

<script>
import { onMounted, onUnmounted, ref } from 'vue';
import gsap from 'gsap';

export default {
    props: [
        'question',
        'yesText',
        'noText'
    ],
    setup(props, { emit }) {

        const el = ref(null)
        onMounted(() => {
            gsap.fromTo(el.value, {
                opacity: 0,
                scale: 0.5
            }, {
                opacity: 1,
                scale: 1,
                duration: 0.2
            })
        })

        const animateLeave = () => {
            gsap.fromTo(el.value, {
                opacity: 1,
                scale: 1
            }, {
                opacity: 0,
                scale: 0.5,
                duration: 0.2
            })
        }

        const handleNo = () => {
            animateLeave()
            setTimeout(() => emit('no'), 200)
        }

        const handleYes = () => {
            animateLeave()
            setTimeout(() => emit('yes'), 200)
        }

        return {
            el,
            handleNo,
            handleYes
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
    gap: 40px
}

.yes-no-modal-wrapper .yes-no-modal div button {
    cursor: pointer;
    color: white;
    padding: 8px 40px;
    font-size: 1.4em;
    width: fit-content;
    align-self: center;
    border: none;
    margin-top: 20px;
    border-radius: 20px;
    box-shadow: 0px 4px 10px -2px rgba(0, 0, 0, 0.5);
}

.yes-no-modal-wrapper .yes-no-modal .yes-button {
    color: rgb(18, 255, 97);
    font-weight: bold;
    transition: 0.3s ease;
}

.yes-no-modal-wrapper .yes-no-modal .yes-button:hover {
    transform: translateY(-4px);
    background-color: rgb(18, 255, 97);
    color: white;
    box-shadow: 0px 8px 10px -2px rgba(18, 255, 97, 0.5);
}

.yes-no-modal-wrapper .yes-no-modal .no-button {
    color: rgb(255, 84, 61);
    font-weight: bold;
    transition: 0.3s ease;
}

.yes-no-modal-wrapper .yes-no-modal .no-button:hover {
    transform: translateY(-4px);
    background-color: rgb(255, 84, 61);
    color: white;
    box-shadow: 0px 8px 10px -2px rgba(255, 84, 61, 0.5);
}
</style>