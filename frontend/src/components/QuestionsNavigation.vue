<template>
    <div class="question-navigation">
        <ul>
            <li v-for="(item, index) in Array(numOfQuestions)" @click="handleClick(index)" :style="{
                backgroundColor: current === index ? 'rgb(94, 158, 255)' : '',
                color: current === index ? 'white' : '',
                transform: current === index ? 'translateY(-4px)' : ''
            }">{{ index + 1
                }}</li>
        </ul>
    </div>
</template>

<script>

import { } from 'vue'
export default {

    setup(props, { emit }) {

        const handleClick = (index) => {
            emit('changeQuestion', index)
        }
        return {
            handleClick
        }
    },
    props: [
        'numOfQuestions',
        'current'
    ]
}
</script>

<style>
.question-navigation {
    margin: auto;
    margin-top: 80px;
    width: 60%;

}

.question-navigation ul {
    list-style: none;
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
}

.question-navigation ul li {
    height: 40px;
    width: 40px;
    border-radius: 20px;
    background-color: white;
    display: flex;
    color: rgb(94, 158, 255);
    border: 2px solid rgb(94, 158, 255);
    justify-content: center;
    align-items: center;
    cursor: pointer;
    font-weight: 700;
    transition: 0.3s ease;
}

.question-navigation ul li:hover {
    background-color: rgb(94, 158, 255);
    color: white;
}
</style>