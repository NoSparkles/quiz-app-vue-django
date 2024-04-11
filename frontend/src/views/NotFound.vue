<template>
    <div>
        <h1>404 Not Found</h1>
        <p>Sorry, the page you are looking for does not exist.</p>
        <RouterLink to="/">Home Page</RouterLink>
    </div>
</template>

<script>
export default {
name: 'NotFound'
}
</script>

<style>
a {
   text-decoration: none;
   color: rgb(53, 165, 240);
   font-size: 1.4em;
}
</style>
