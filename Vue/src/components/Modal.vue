<template>
    <transition name="modal">
        <div class="modal-mask">
          <div class="modal-wrapper" @click="$emit('close')">
            <div class="modal-container" @click.stop>

              <div class="modal-header">
                <slot name="header">
                  Instrukcja
                </slot>
              </div>

              <div class="modal-body">
                <slot name="body">
                    <p>Aplikacja 1: Napełnianie zbiornika - niesterowane</p>
                    <p>
                        Symuluje napełnianie zbiornika z jednego wlewu o stałym przepływie i wypływie zależnym od parametrów beta i od wysokości początkowej słupa wody. Im wyższy słup wody, tym więcej jej wypływa, lecz jeśli poziom wody osiągnie wartość większą niż maksymalna zdefiniowana lub zbiornik zostanie opróżniony, to symulacja zostanie przerwana. 
                        <!--<ul>
                        <li>A - powierzchnia podstawy zbiornika (w m^2)</li>
                        <li>Beta - współczynnik wypływu cieczy (im mniejszy tym wolniejszy wypływ; w m^(5/2)/s)</li>
                        <li>Qd - wpływ wody (w m^3/s)</li>
                        <li>H - początkowa wysokość zbiornika wody (w m)</li>
                        <li>hMax - maksymalna wysokość zbiornika wody (w m)</li>
                        <li>Tp - krok czasowy (w s)</li>
                        <li>simLength - długość symulacji (w h)</li>
                        </ul>-->
                    </p>
                    <br/>
                    <p>Aplikacja 2: Symulacja mieszania - niesterowane</p>
                    <p>
                        Symuluje napełnianie zbiornika z dwóch źródeł o różnych stężeniach jakiejś substancji w nich zawartych. Wypływ cieczy jest stały i niezmienny w czasie. Jeśli przekroczona zostanie pojemność maksymalna lub opróżnimy zbiornik do zera, symulacja zostanie przerwana.
                        <!--<ul>
                        <li>V - pojemność początkowa (w m^3)</li>
                        <li>c - stężenie początkowe (w zakresie &#60;0, 1>, gdzie 0 to 0% stężenia, a 1 to 100% stężenia.</li>
                        <li>Qd1 - wpływ cieczy ze źródła pierwszego (w m^3/s)</li>
                        <li>Qd2 - wpływ cieczy ze źródła drugiego (w m^3/s)</li>
                        <li>Qo - wypływ cieczy ze zbiornika (w m^3/s)</li>
                        <li>cd1 - stężenie substancji we wpływie pierwszym (w zakresie &#60;0,1>)</li>
                        <li>cd2 - stężenie substancji we wpływie drugim (w zakresie &#60;0,1>)</li>
                        <li>Tp - krok czasowy symulacji (w s)</li>
                        <li>simLength - długość symulacji (w h)</li>
                        <li>vMax - maksymalna objętość zbiornika (w m^3)</li>
                        </ul>-->
                    </p>
                    <br/>
                    <p>Aplikacja 3: Symulacja napełniania ze sterowaniem - sterowane regulatorem PID</p>
                    <p>
                        Symuluje napełnianie zbiornika z jednego wlewu sterowanym regulatorem PID i wypływie zależnym od parametrów beta i od wysokości początkowej słupa wody. Im wyższy słup wody, tym więcej jej wypływa, lecz jeśli poziom wody osiągnie wartość większą niż maksymalna zdefiniowana lub zbiornik zostanie opróżniony, to symulacja zostanie przerwana. 
                        <!--<ul>
                        <li>A - powierzchnia podstawy zbiornika (w m^2)</li>
                        <li>Beta - współczynnik wypływu cieczy (im mniejszy tym wolniejszy wypływ; w m^(5/2)/s)</li>
                        <li>Qd - wpływ wody (w m^3/s)</li>
                        <li>H - początkowa wysokość zbiornika wody (w m)</li>
                        <li>hMax - maksymalna wysokość zbiornika wody (w m)</li>
                        <li>Tp - krok czasowy (w s)</li>
                        <li>simLength - długość symulacji (w h)</li>
                        <li>target_level - docelowy poziom wody do którego dąży regulator (w m)</li>
                        <li>maxInput - maksymalna wartość wpływu wody (w m^3/s)</li>
                        <li>P1 - współczynnik proporcjonalny regulatora PID, wartość 0 oznacza wyłączenie regulatora całkowicie).</li>
                        <li>I1 - czas zdwojenia części całkującej. Im większa, tym część całkująca wolniej reaguje.</li>
                        <li>D1 - czas wyprzedzenia części różniczkującej. Im większa tym reglator wolniej (słabiej) reaguje na zmiany.</li>
                        <li>version - używane, gdy chcemy aby algorytm uczony maszynowo sam dobrał parametry regulatora PID. Wartość 0 oznacza algorytm regresji liniowej, wartość 1 oznacza uczony algorytm genetryczny.</li>
                        </ul>
                    </p>
                    <br/>
                    <p>Aplikacja 3.1: Symulacja napełniania ze sterowaniem (AI)</p>
                    <p>-->
                        
                    </p>
                    <br/>
                    <p>Aplikacja 4: Symulacja mieszania - sterowane regulatorami PID</p>
                    <p>
                        Symuluje napełnianie zbiornika z dwóch źródeł o różnych stężeniach jakiejś substancji w nich zawartych. Posiada 3 regulatory PID: dwa ustawione kaskadowo do regulowania wpływu cieczy pierwszej, a trzeci na wypływie aby regulować poziom wody w zbiorniku. Jeśli przekroczona zostanie pojemność maksymalna lub opróżnimy zbiornik do zera, symulacja zostanie przerwana.
                        <!--<ul>
                        <li>V - pojemność początkowa (w m^3)</li>
                        <li>c - stężenie początkowe (w zakresie &#60;0, 1>, gdzie 0 to 0% stężenia, a 1 to 100% stężenia.</li>
                        <li>Qd1 - wpływ cieczy ze źródła pierwszego (w m^3/s)</li>
                        <li>Qd2 - wpływ cieczy ze źródła drugiego (w m^3/s)</li>
                        <li>Qo - wypływ cieczy ze zbiornika (w m^3/s)</li>
                        <li>cd1 - stężenie substancji we wpływie pierwszym (w zakresie &#60;0,1>)</li>
                        <li>cd2 - stężenie substancji we wpływie drugim (w zakresie &#60;0,1>)</li>
                        <li>Tp - krok czasowy symulacji (w s)</li>
                        <li>simLength - długość symulacji (w h)</li>
                        <li>P1 - współczynnik proporcjonalny regulatorów PID, wartość 0 oznacza wyłączenie regulatora całkowicie). (Regulatory połączone kaskadowo mają te same parametry)</li>
                        <li>I1 - czas zdwojenia części całkujących. Im większa, tym część całkująca wolniej reaguje. (Regulatory połączone kaskadowo mają te same parametry)</li>
                        <li>D1 - czas wyprzedzenia części różniczkujących. Im większa tym reglator wolniej (słabiej) reaguje na zmiany. (Regulatory połączone kaskadowo mają te same parametry)</li>
                        <li>maxInput - maksymalny wpływ cieczy z wejścia pierwszego (w m^3/s)</li>
                        <li>vMax - maksymalna objętość zbiornika (w m^3)</li>
                        <li>P2 - współczynnik proporcjonalny regulatora PID, wartość 0 oznacza wyłączenie regulatora całkowicie).</li>
                        <li>I2 - czas zdwojenia części całkujących. Im większa, tym część całkująca wolniej reaguje.</li>
                        <li>D2 - czas wyprzedzenia części różniczkujących. Im większa tym reglator wolniej (słabiej) reaguje na zmiany.</li>
                        </ul>-->
                    </p>
                    <br/>
                    <p>Aplikacja 5: Symulacja napełniania - regulator rozmyty</p>
                    <p>
                        Aplikacja służy do zasymulowania działania napełniania zbiornika ze sterowanym dopływem i grawitacyjnym odpływem. Za utrzymanie ustalonego poziomu odpowiada regulator rozmyty
                    </p>
                </slot>
              </div>

              <div class="modal-footer">
                <slot name="footer">
                  <button class="modal-default-button" @click="$emit('close')">
                    OK
                  </button>
                </slot>
              </div>
            </div>
          </div>
        </div>
      </transition>
</template>

<script>
export default {
    name: 'InfoModal',
    // data(){
    //     return {
    //         showModal: true,
    //     }
    // },
    // methods: {
    //     showInfoModal(){

    //     },
    // }
};

</script>

<style lang="scss">
@import "@/scss/variables.scss";
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  overflow: auto;
  height: 80%;
  width: 80%;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
  text-align: initial;
}

.modal-default-button {
  float: right;
}

ul {
  padding: 0 30px;
}
</style>