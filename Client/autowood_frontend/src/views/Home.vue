<template>
    
    <section class="hero is-small is-primary mb-6" style="background-color: rgb(242, 248, 254);">
        <div class="hero-body">
          <p class="title" style="color: rgb(120, 157, 188);">Dzień dobry! Od czego dzisiaj zaczniesz?  
          </p>
          
        </div>
      </section>

      <div class="container">
      <div class="columns">
        <div class="column is-half is-offset-one-quarter">
          <div class="card">
            <header  class="card-header" style="background-color: rgb(242, 248, 254) ;">
              <p class="card-header-title is-centered is-size-4" style="color: rgb(120, 157, 188);">Na skróty &nbsp;<i class="fa-solid fa-arrow-up-right-from-square"></i></p>
              
            </header>


            <div class="card-content" style="background-color: rgb(242, 248, 254) ;">
              <div class="content">
                <div class="columns">
                  <div class="column is-half">
                    <div class="container">
                      <ul class="is-size-5">
                        <li class="is-size-5">
                          <router-link to="/projects-list">Lista projektów i wycen</router-link>
                        </li>
                        <li >
                          <router-link to="/new-project">Nowa wycena</router-link>
                        </li>
                      </ul>
                    </div>

                  </div>
                  <div class="column is-half">
                    <div class="container">
                      <ul class="is-size-5">
                        
                        <li >
                          <router-link to="/accesories">Zarządzaj akcesoriami</router-link>
                        </li>
                        <li >
                          <router-link to="/prices-setup">Zarządzaj kosztami pracy</router-link>
                        </li>
                      </ul>
                    </div>

                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
</template>

<script setup>

</script>

<style>
.card {
  --bulma-card-radius: 0.3rem;
}

a{
  color: #0333b4;
}
</style>