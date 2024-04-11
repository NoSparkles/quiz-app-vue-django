<template>
    <div class="quiz-toast">
        You have not selected all answers
    </div>
</template>

<script>
export default {
    setup(props, { emit }) {
        setTimeout(() => {
            emit('close')
        }, 3000);
        return {

        }
    }
}
</script>

<style>
.quiz-toast {
    position: absolute;
    background-color: rgb(255, 118, 140);
    padding: 20px 80px;
    border-radius: 20px;
    margin-top: 20px;
    color: white;
    font-size: 1.2em;
}
</style>