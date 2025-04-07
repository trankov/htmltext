from htmltext import text_from_html


html = r"""



<!DOCTYPE html>
<html class="h-100" lang="ru">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="htmx-config"
          content='{"responseHandling": [{"code":".*", "swap": true}]}' />
    <title>


    Все сборы


    </title>
    <link rel="stylesheet"
          href="/static/website/assets/nocdn/bootstrap%405.3.3/dist/css/bootstrap.min.css" />
    <link rel="stylesheet"
          href="/static/website/assets/nocdn/bootstrap-icons%401.11.3/font/bootstrap-icons.min.css" />
    <link rel="stylesheet" href="/static/website/assets/styles/main.css" />
    <link rel="stylesheet" href="/static/website/assets/styles/user.css" />

  <script defer
          src="/static/website/assets/nocdn/hyperscript.org%400.9.13/dist/_hyperscript.min.js"></script>

  </head>

  <body class="pp-bg-grey h-100">



      <div class="pp-bg d-none d-md-block"></div>

      <div class="container-fluid h-100">
        <!-- button sidebar -->
        <div class="d-md-none position-absolute start-0 m-1">
          <button type="button"
                  class="btn"
                  data-bs-toggle="offcanvas"
                  data-bs-target="#pp-sidebar-offcanvas">
            <i class="fs-4 bi bi-list"></i>
          </button>
        </div>


  <!-- button phone -->
  <div class="d-xl-none position-absolute end-0 m-1">
    <button type="button"
            class="btn"
            data-bs-toggle="offcanvas"
            data-bs-target="#pp-phone-offcanvas">
      <i class="fs-4 bi bi-phone"></i>
    </button>
  </div>


        <!-- content -->
        <div class="row min-h-100 flex-nowrap">
          <!-- block sidebar -->
          <div class="pp-bg-ltgrey col-md-4 col-lg-3 col-xxl-2 overflow-y-auto vh-100 sticky-md-top offcanvas-md offcanvas-start"
               data-bs-scroll="false"
               data-bs-backdrop="false"
               tabindex="-1"
               id="pp-sidebar-offcanvas">
            <div class="offcanvas-header position-absolute p-0 mt-3">
              <button type="button"
                      class="btn-close"
                      data-bs-dismiss="offcanvas"
                      data-bs-target="#pp-sidebar-offcanvas"></button>
            </div>

            <div class="offcanvas-body py-0 px-4">
              <nav class="d-flex flex-column align-items-center w-100">
                <img class="pp-logo mt-5"
                     src="/static/website/assets/images/logo-yellow.svg" />

                <div class="d-md-block d-flex flex-column align-items-center w-100">
                  <div class="pp-text-main-bold text-break mt-3">
                    <script>
                      document.write('prodpapa+trankov@ya.ru'.replace(/([@\.-])/g, '\u200B$1\u200B').replace(/\u200B\u200B/g, '\u200B'));
                    </script>
                  </div>

                  <div class="mt-3">
                    <a href="/business/auth/logout"
                       class="pp-text-small-dkgrey td-none">
                      <i class="bi bi-box-arrow-in-left"></i>
                      Выйти из аккаунта
                    </a>
                  </div>

                  <div class="mt-5">
                    <a href="/business/gather/basic-new"
                       class="pp-btn-yellow pp-btn-sm-1 btn w-100">
                      <svg width="10" height="13">
                        <rect x="3.75" width="2.5" height="10" fill="black" />
                        <rect y="3.75" width="10" height="2.5" fill="black" />
                      </svg>
                      новый сбор
                    </a>
                  </div>

                  <div class="pp-text-title mt-5">Аккаунт</div>

                  <div class="mt-1">
                    <a href="/business/personal"
                       class="pp-text-main td-none">О пользователе</a>
                  </div>

                  <div class="mt-1">
                    <a href="/business/notifications"
                       class="pp-text-main td-none">
                      Уведомления

                    </a>
                  </div>

                  <div class="pp-text-title mt-4">Сборы</div>




                  <div class="mt-1">
                    <a href="/business/gather/basic-new"
                       class="pp-nav-active pp-text-main td-none">Все сборы</a>
                  </div>

                  <div class="my-5">
                    <a href="#"
                       class="pp-text-main pp-color-dkgrey td-none"
                       data-bs-target="#pp-modal-questions"
                       data-bs-toggle="modal">
                      <i class="bi bi-question-circle"></i>
                      Есть вопросы?
                    </a>
                  </div>
                </div>
              </nav>
            </div>
          </div>


  <!-- block main -->
  <div class="col px-md-5">
    <div class="row">
      <div class="col my-5">

  <!-- dashboard -->

    <h1 class="pp-text-heading">Все сборы</h1>

    <div class="pp-text-lead mt-3 mb-5">
      Здесь будут показаны все ваши сборы. Тут пока ничего нет,
      поэтому предлагаем сразу заполнить необходимые поля для открытия первого сбора
    </div>



        <!-- details -->


  <h3 class="my-0 pt-4 pb-0">
    <a href="#"
       class="pp-text-heading pp-active-section-heading td-none d-inline-block w-100 collapsed"
       data-bs-toggle="collapse"
       data-bs-target="#section_general">

      Общая информация
      <i class="float-end bi bi-caret-up-fill"></i>
    </a>
  </h3>

  <div id="section_general"
       class="collapse pp-active-section ">
    <form class="pp-form row g-3 mt-0 pb-5" method="post">
      <input type="hidden" name="csrfmiddlewaretoken" value="KRGsY2yOT9oqCbDAWG5bts1or8TIgiypG5FRuUT4pmo5e3lLQsFXxLLZBNyfVmEv"><input type="hidden" name="user" value="1" id="id_user">



      <div class="col-12">
        <label for="" class="form-label">Название компании</label>



        <input type="text" name="title" class="form-control" id="title" placeholder="Например, Отличный стартап" required autofocus maxlength="300">
      </div>

      <div class="col-12">
        <label for="" class="form-label">
          Сайт компании

          <a class="td-none"
             tabindex="0"
             data-bs-toggle="popover"
             data-bs-trigger="focus"
             data-bs-content="Ограничение 40 символов">
            <i class="bi bi-question-circle"></i>
          </a>
        </label>



        <input type="text" name="website_url" class="form-control" id="website_url" placeholder="Например, mos.ru" required maxlength="200">
      </div>

      <div class="col-12">
        <label for="" class="form-label">Категория бизнеса</label>



        <select name="category" class="form-select" id="category" required>
  <option value="" selected>---------</option>

  <option value="1">Развлечения</option>

  <option value="2">Финансы</option>

  <option value="3">Производство</option>

  <option value="4">E-commerce</option>

  <option value="5">Ритейл</option>

  <option value="6">Логистика</option>

  <option value="7">Авто</option>

  <option value="8">Страхование</option>

  <option value="9">Консалтинг</option>

  <option value="10">IT и SaaS</option>

  <option value="11">Сельхоз</option>

  <option value="12">Туризм</option>

  <option value="13">ВЭД</option>

  <option value="14">Аренда</option>

  <option value="15">Маркетплейсы</option>

  <option value="16">Склады</option>

  <option value="17">Строительство</option>

  <option value="18">Медицина</option>

  <option value="19">Мероприятия</option>

  <option value="20">Услуги</option>

  <option value="21">СМИ</option>

  <option value="22">Образование</option>

</select>
      </div>


  <div class="col-12 mt-md-5">
    <button type="submit" class="pp-btn-black btn w-100">Разблокировать конструктор</button>
  </div>

    </form>
  </div>



  <h3 class="my-0 pt-4 pb-0">
    <a href="#"
       class="pp-text-heading td-none d-inline-block w-100 disabled collapsed">
      <i class="h5 bi bi-lock-fill"></i>
      Дизайн
      <i class="float-end bi bi-caret-up-fill"></i>
    </a>
  </h3>



  <h3 class="my-0 pt-4 pb-0">
    <a href="#"
       class="pp-text-heading td-none d-inline-block w-100 disabled collapsed">
      <i class="h5 bi bi-lock-fill"></i>
      Цифры сбора
      <i class="float-end bi bi-caret-up-fill"></i>
    </a>
  </h3>



  <h3 class="my-0 pt-4 pb-0">
    <a href="#"
       class="pp-text-heading td-none d-inline-block w-100 disabled collapsed">
      <i class="h5 bi bi-lock-fill"></i>
      Видео рилс
      <i class="float-end bi bi-caret-up-fill"></i>
    </a>
  </h3>



  <h3 class="my-0 pt-4 pb-0">
    <a href="#"
       class="pp-text-heading td-none d-inline-block w-100 disabled collapsed">
      <i class="h5 bi bi-lock-fill"></i>
      Юр.информация
      <i class="float-end bi bi-caret-up-fill"></i>
    </a>
  </h3>



  <h3 class="my-0 pt-4 pb-0">
    <a href="#"
       class="pp-text-heading td-none d-inline-block w-100 disabled collapsed">
      <i class="h5 bi bi-lock-fill"></i>
      Подпись по СМС
      <i class="float-end bi bi-caret-up-fill"></i>
    </a>
  </h3>

      </div>

      <!-- block phone -->
      <div class="col overflow-y-auto vh-100 sticky-xl-top offcanvas-xl offcanvas-end"
           data-bs-scroll="false"
           data-bs-backdrop="false"
           tabindex="-1"
           id="pp-phone-offcanvas">
        <div class="offcanvas-header position-absolute end-0 p-0 mt-3 me-3">
          <button type="button"
                  class="btn-close"
                  data-bs-dismiss="offcanvas"
                  data-bs-target="#pp-phone-offcanvas"></button>
        </div>

        <div class="offcanvas-body d-flex justify-content-center p-0">
          <div class="w-100 mx-3 my-5">
            <div class="pp-phone-container w-100 mx-auto">
              <div class="pp-phone-wrapper position-relative">

  <div class="position-absolute w-100 h-100"
     style="font-size: 1em;
            padding: 4.6% 5.8% 4.6% 5.2%">
  <div class="position-relative overflow-hidden d-flex flex-column align-items-center h-100"
       style="border-radius: 2em;
              background-color: white">
    <div class="position-absolute" style="top: 0; left: 0; right: 0">
      <svg class="position-absolute w-100"
           viewBox="0 0 375 44"
           fill="none"
           xmlns="http://www.w3.org/2000/svg">
        <path opacity="0.35" d="M334.667 17.8333H351.334C352.53 17.8333 353.5 18.8033 353.5 19.9999V25.9999C353.5 27.1965 352.53 28.1666 351.334 28.1666H334.667C333.47 28.1666 332.5 27.1965 332.5 25.9999V19.9999C332.5 18.8033 333.47 17.8333 334.667 17.8333Z" stroke="black" />
        <path opacity="0.4" d="M355 20.9999V24.9999C355.805 24.6611 356.328 23.873 356.328 22.9999C356.328 22.1267 355.805 21.3387 355 20.9999" fill="black" />
        <path d="M334 20.4333C334 19.8257 334.493 19.3333 335.1 19.3333H350.9C351.508 19.3333 352 19.8257 352 20.4333V25.5666C352 26.1741 351.508 26.6666 350.9 26.6666H335.1C334.493 26.6666 334 26.1741 334 25.5666V20.4333Z" fill="black" />
        <path fill-rule="evenodd" clip-rule="evenodd" d="M319.331 19.6079C321.547 19.608 323.678 20.4594 325.284 21.9862C325.405 22.1041 325.598 22.1026 325.717 21.9829L326.873 20.8162C326.933 20.7555 326.967 20.6733 326.966 20.5877C326.966 20.5021 326.931 20.4202 326.87 20.3602C322.655 16.3207 316.005 16.3207 311.79 20.3602C311.729 20.4202 311.695 20.502 311.694 20.5876C311.694 20.6732 311.727 20.7555 311.787 20.8162L312.944 21.9829C313.063 22.1028 313.256 22.1043 313.377 21.9862C314.983 20.4593 317.115 19.6079 319.331 19.6079ZM319.331 23.4036C320.548 23.4035 321.722 23.856 322.625 24.6732C322.747 24.7892 322.939 24.7867 323.058 24.6676L324.213 23.5009C324.274 23.4397 324.307 23.3567 324.306 23.2704C324.305 23.1842 324.27 23.1018 324.208 23.0419C321.46 20.4855 317.204 20.4855 314.456 23.0419C314.394 23.1018 314.358 23.1842 314.357 23.2705C314.357 23.3568 314.39 23.4398 314.451 23.5009L315.606 24.6676C315.725 24.7867 315.917 24.7892 316.039 24.6732C316.941 23.8566 318.114 23.4041 319.331 23.4036ZM321.644 25.9574C321.645 26.0439 321.611 26.1273 321.55 26.1879L319.552 28.2036C319.494 28.2628 319.414 28.2961 319.331 28.2961C319.247 28.2961 319.168 28.2628 319.109 28.2036L317.111 26.1879C317.05 26.1272 317.016 26.0438 317.018 25.9573C317.019 25.8708 317.057 25.7889 317.121 25.7309C318.397 24.652 320.265 24.652 321.54 25.7309C321.605 25.7889 321.642 25.8709 321.644 25.9574Z" fill="black" />
        <path fill-rule="evenodd" clip-rule="evenodd" d="M305.667 17.6665H304.667C304.115 17.6665 303.667 18.1142 303.667 18.6665V27.3332C303.667 27.8855 304.115 28.3332 304.667 28.3332H305.667C306.219 28.3332 306.667 27.8855 306.667 27.3332V18.6665C306.667 18.1142 306.219 17.6665 305.667 17.6665ZM300 19.9998H301C301.553 19.9998 302 20.4476 302 20.9998V27.3332C302 27.8855 301.553 28.3332 301 28.3332H300C299.448 28.3332 299 27.8855 299 27.3332V20.9998C299 20.4476 299.448 19.9998 300 19.9998ZM296.334 22.3332H295.334C294.781 22.3332 294.334 22.7809 294.334 23.3332V27.3332C294.334 27.8855 294.781 28.3332 295.334 28.3332H296.334C296.886 28.3332 297.334 27.8855 297.334 27.3332V23.3332C297.334 22.7809 296.886 22.3332 296.334 22.3332ZM291.667 24.3332H290.667C290.115 24.3332 289.667 24.7809 289.667 25.3332V27.3332C289.667 27.8855 290.115 28.3332 290.667 28.3332H291.667C292.219 28.3332 292.667 27.8855 292.667 27.3332V25.3332C292.667 24.7809 292.219 24.3332 291.667 24.3332Z" fill="black" />
      </svg>

      <div class="position-absolute" style="top: .6em;left: 1.5em;right: 50%">
        <div class="position-absolute w-100 text-truncate"
             style="font-family: 'TT Travels Trl';
                    font-size: 75%;
                    font-weight: 600;
                    transform: scale(.95, 1);
                    color: black"
             _="init repeat forever make a Date put it.toLocaleTimeString('ru-ru', {hour: '2-digit', minute:'2-digit'}) into me wait 1s end">
          <script>document.write((new Date()).toLocaleTimeString('ru-ru', {hour: '2-digit', minute:'2-digit'}))</script>
        </div>
      </div>
    </div>

    <div class="position-absolute overflow-hidden"
         style="top: 2.4em;
                bottom: 5.5em;
                left: .7em;
                right: .7em;
                border-radius: 1em">
      <div class="position-absolute"
           style="top: 0;
                  bottom: 0;
                  left: 0;
                  right: 0;
                  background-color: #bdbdbd">

          <svg class="position-absolute top-50 start-50 translate-middle"
               style="width: 3em"
               viewBox="0 0 48 36"
               fill="none"
               xmlns="http://www.w3.org/2000/svg">
            <path d="M45 30C45 30.7957 44.6839 31.5587 44.1213 32.1213C43.5587 32.6839 42.7957 33 42 33H6C5.20435 33 4.44129 32.6839 3.87868 32.1213C3.31607 31.5587 3 30.7957 3 30V12C3 11.2044 3.31607 10.4413 3.87868 9.87868C4.44129 9.31607 5.20435 9 6 9H9.516C11.9017 8.99869 14.1893 8.05021 15.876 6.363L18.366 3.879C18.927 3.31782 19.6875 3.00176 20.481 3H27.513C28.3086 3.00017 29.0715 3.31635 29.634 3.879L32.118 6.363C32.9539 7.19914 33.9463 7.8624 35.0386 8.31486C36.1309 8.76733 37.3017 9.00014 38.484 9H42C42.7957 9 43.5587 9.31607 44.1213 9.87868C44.6839 10.4413 45 11.2044 45 12V30ZM6 6C4.4087 6 2.88258 6.63214 1.75736 7.75736C0.632141 8.88258 0 10.4087 0 12V30C0 31.5913 0.632141 33.1174 1.75736 34.2426C2.88258 35.3679 4.4087 36 6 36H42C43.5913 36 45.1174 35.3679 46.2426 34.2426C47.3679 33.1174 48 31.5913 48 30V12C48 10.4087 47.3679 8.88258 46.2426 7.75736C45.1174 6.63214 43.5913 6 42 6H38.484C36.8928 5.99966 35.367 5.3673 34.242 4.242L31.758 1.758C30.633 0.632704 29.1072 0.000339824 27.516 0H20.484C18.8928 0.000339824 17.367 0.632704 16.242 1.758L13.758 4.242C12.633 5.3673 11.1072 5.99966 9.516 6H6Z" fill="#F2F1F5" />
            <path d="M24 27C22.0109 27 20.1032 26.2098 18.6967 24.8033C17.2902 23.3968 16.5 21.4891 16.5 19.5C16.5 17.5109 17.2902 15.6032 18.6967 14.1967C20.1032 12.7902 22.0109 12 24 12C25.9891 12 27.8968 12.7902 29.3033 14.1967C30.7098 15.6032 31.5 17.5109 31.5 19.5C31.5 21.4891 30.7098 23.3968 29.3033 24.8033C27.8968 26.2098 25.9891 27 24 27ZM24 30C26.7848 30 29.4555 28.8938 31.4246 26.9246C33.3938 24.9555 34.5 22.2848 34.5 19.5C34.5 16.7152 33.3938 14.0445 31.4246 12.0754C29.4555 10.1062 26.7848 9 24 9C21.2152 9 18.5445 10.1062 16.5754 12.0754C14.6062 14.0445 13.5 16.7152 13.5 19.5C13.5 22.2848 14.6062 24.9555 16.5754 26.9246C18.5445 28.8938 21.2152 30 24 30ZM9 13.5C9 13.8978 8.84196 14.2794 8.56066 14.5607C8.27936 14.842 7.89782 15 7.5 15C7.10218 15 6.72064 14.842 6.43934 14.5607C6.15804 14.2794 6 13.8978 6 13.5C6 13.1022 6.15804 12.7206 6.43934 12.4393C6.72064 12.158 7.10218 12 7.5 12C7.89782 12 8.27936 12.158 8.56066 12.4393C8.84196 12.7206 9 13.1022 9 13.5Z" fill="#F2F1F5" />
          </svg>

      </div>

      <div class="position-absolute"
           style="top: .85em;
                  bottom: 1em;
                  left: 1em;
                  right: 1em">
        <div class="position-absolute" style="top: 0; left: 0; right: 0">
          <div class="position-absolute w-100 text-truncate"
               style="font-family: 'TT Travels Trl';
                      font-size: 125%;
                      font-weight: 800;
                      color: white">Название компании</div>
        </div>

        <div class="position-absolute" style="top: 2.25em; left: 0; right: 0">
          <div class="position-absolute" style="top: 0; left: 0; right: 50%">
            <div class="position-absolute w-100 text-truncate"
                 style="font-family: 'Fira Sans';
                        font-size: 80%;
                        font-weight: 500;
                        letter-spacing: -.025em;
                        color: white">

                Собрано, ₽

            </div>
          </div>

          <div class="position-absolute" style="top: 0; left: 50%; right: 0">
            <div class="position-absolute w-100 text-truncate text-end"
                 style="font-family: 'Fira Sans';
                        font-size: 80%;
                        font-weight: 500;
                        letter-spacing: -.025em;
                        color: white">

                Сумма, ₽

            </div>
          </div>

          <div class="position-absolute" style="top: 1.35em; left: 0; right: 0">
            <div class="position-absolute w-100"
                 style="background-color: white;
                        height: .25em;
                        border-radius: 2em">&nbsp;</div>
          </div>
        </div>

        <div class="position-absolute" style="bottom: 0; left: 0; right: 0">
          <div class="position-absolute w-100 text-center text-truncate"
               style="bottom: 0;
                      font-size: 75%;
                      background-color: white;
                      padding: .24em .5em;
                      border-radius: .5em">Описание</div>
        </div>
      </div>
    </div>

    <div class="position-absolute" style="bottom: 5.8em; left: 0; right: 0">
      <svg class="position-absolute w-100"
           viewBox="0 0 385 83"
           fill="none"
           xmlns="http://www.w3.org/2000/svg">
        <path d="M5 50C5 31.1438 5 21.7157 10.8579 15.8579C16.7157 10 26.1438 10 45 10H340C358.856 10 368.284 10 374.142 15.8579C380 21.7157 380 31.1438 380 50V83H5V50Z" fill="white" />
        <path fill-rule="evenodd" clip-rule="evenodd" d="M82.5 38C82.5 37.4477 82.9477 37 83.5 37H91.5C92.0523 37 92.5 37.4477 92.5 38L92.5 38.0017C94.675 38.0138 95.8529 38.1103 96.6213 38.8787C97.3814 39.6387 97.484 40.7994 97.4978 42.9294C97.4913 44.343 97.4647 45.4313 97.3576 46.3132C97.2197 47.4483 96.9612 48.1066 96.5416 48.5978C96.4055 48.7571 96.2571 48.9055 96.0978 49.0416C95.6066 49.4612 94.9484 49.7197 93.8132 49.8576C92.6547 49.9983 91.1401 50 89 50H86C83.8599 50 82.3453 49.9983 81.1868 49.8576C80.0516 49.7197 79.3934 49.4612 78.9022 49.0416C78.7429 48.9055 78.5945 48.7571 78.4584 48.5978C78.0388 48.1066 77.7803 47.4483 77.6424 46.3132C77.5353 45.4313 77.5087 44.343 77.5022 42.9294C77.516 40.7994 77.6186 39.6387 78.3787 38.8787C79.1471 38.1103 80.325 38.0138 82.5 38.0017L82.5 38ZM97.5 48.9938C97.4379 49.0809 97.372 49.1653 97.302 49.2472C97.1319 49.4464 96.9464 49.6319 96.7472 49.802C95.3446 51 93.2297 51 89 51H86C81.7703 51 79.6554 51 78.2528 49.802C78.0536 49.6319 77.8681 49.4464 77.698 49.2472C77.628 49.1653 77.5621 49.0809 77.5 48.9938V51C77.5 53.8284 77.5 55.2426 78.3787 56.1213C79.2574 57 80.6716 57 83.5 57H91.5C94.3284 57 95.7426 57 96.6213 56.1213C97.5 55.2426 97.5 53.8284 97.5 51V48.9938ZM85.5 44C84.9477 44 84.5 44.4477 84.5 45C84.5 45.5523 84.9477 46 85.5 46H89.5C90.0523 46 90.5 45.5523 90.5 45C90.5 44.4477 90.0523 44 89.5 44H85.5Z" fill="#BDBDBD" />
        <path fill-rule="evenodd" clip-rule="evenodd" d="M183.964 38.4645C182.5 39.9289 182.5 42.286 182.5 47C182.5 51.714 182.5 54.0711 183.964 55.5355C185.429 57 187.786 57 192.5 57C197.214 57 199.571 57 201.036 55.5355C202.5 54.0711 202.5 51.714 202.5 47C202.5 42.286 202.5 39.9289 201.036 38.4645C199.571 37 197.214 37 192.5 37C187.786 37 185.429 37 183.964 38.4645ZM188.5 44C187.948 44 187.5 44.4477 187.5 45V52C187.5 52.5523 187.948 53 188.5 53C189.052 53 189.5 52.5523 189.5 52V45C189.5 44.4477 189.052 44 188.5 44ZM191.5 43C191.5 42.4477 191.948 42 192.5 42C193.052 42 193.5 42.4477 193.5 43V52C193.5 52.5523 193.052 53 192.5 53C191.948 53 191.5 52.5523 191.5 52V43ZM196.5 47C195.948 47 195.5 47.4477 195.5 48V52C195.5 52.5523 195.948 53 196.5 53C197.052 53 197.5 52.5523 197.5 52V48C197.5 47.4477 197.052 47 196.5 47Z" fill="#BDBDBD" />
        <path fill-rule="evenodd" clip-rule="evenodd" d="M297.5 47C300.261 47 302.5 44.7614 302.5 42C302.5 39.2386 300.261 37 297.5 37C294.739 37 292.5 39.2386 292.5 42C292.5 44.7614 294.739 47 297.5 47ZM289.715 50.2439C288.979 50.5504 288.5 51.269 288.5 52.0658C288.5 54.7909 290.709 57 293.434 57H301.566C304.291 57 306.5 54.7909 306.5 52.0658C306.5 51.269 306.021 50.5504 305.285 50.2439L303.269 49.4038C299.577 47.8654 295.423 47.8654 291.731 49.4038L289.715 50.2439Z" fill="#BDBDBD" />
      </svg>
    </div>

    <div class="position-absolute" style="bottom: 1.6em; left: 0; right: 0">
      <svg class="position-absolute w-100"
           viewBox="0 0 375 34"
           fill="none"
           xmlns="http://www.w3.org/2000/svg">
        <rect width="375" height="34" fill="white" />
        <rect x="121" y="21" width="134" height="5" rx="2.5" fill="black" />
      </svg>
    </div>
  </div>
</div>

<svg class="position-absolute w-100"
     viewBox="0 0 338 682"
     fill="none"
     xmlns="http://www.w3.org/2000/svg">
  <path fill-rule="evenodd" clip-rule="evenodd" d="M51.6 0.000183105C24.2067 0.000183105 2.00002 22.2199 2.00002 49.6293V140.082C1.11637 140.082 0.400024 140.799 0.400024 141.683V164.897C0.400024 165.781 1.11637 166.498 2.00002 166.498V188.11C1.11637 188.11 0.400024 188.827 0.400024 189.711V238.54C0.400024 239.424 1.11637 240.141 2.00002 240.141V253.749C1.11637 253.749 0.400024 254.466 0.400024 255.35V304.179C0.400024 305.063 1.11637 305.779 2.00002 305.779V632.371C2.00002 659.78 24.2067 682 51.6 682H284.4C311.793 682 334 659.78 334 632.371V286.568H335.6C336.484 286.568 337.2 285.851 337.2 284.967V207.322C337.2 206.438 336.484 205.721 335.6 205.721H334V49.6293C334 22.2199 311.793 0.000183105 284.4 0.000183105H51.6ZM17.9932 49.6295C17.9932 31.0618 33.0364 16.0098 51.5932 16.0098H102.06C105.193 16.0098 105.993 18.0082 105.993 21.0985C105.993 30.8876 108.393 40.4241 122.908 40.4241H213.079C227.593 40.4241 229.993 30.8876 229.993 21.0985C229.993 18.0082 230.793 16.0098 233.926 16.0098H284.393C302.95 16.0098 317.993 31.0618 317.993 49.6295V632.371C317.993 650.939 302.95 665.991 284.393 665.991H51.5932C33.0364 665.991 17.9932 650.939 17.9932 632.371V49.6295Z" fill="#B6A8F0" />
  <path d="M140.4 4.80298H197.2V6.40392C197.2 8.17227 195.767 9.60579 194 9.60579H143.6C141.832 9.60579 140.4 8.17227 140.4 6.40392V4.80298Z" fill="#9581E9" />
  <path d="M128.681 24.0908C128.681 26.3435 126.827 28.1697 124.541 28.1697C122.254 28.1697 120.4 26.3435 120.4 24.0908C120.4 21.838 122.254 20.0118 124.541 20.0118C126.827 20.0118 128.681 21.838 128.681 24.0908Z" fill="#9581E9" />
</svg>


              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- append extra modal dialogs here -->


          <!-- modal questions -->
          <div class="modal fade" id="pp-modal-questions" tabindex="-1">
            <div class="modal-dialog modal-dialog-centered">
              <div class="modal-content">
                <div class="modal-header">
                  <h4 class="pp-text-heading modal-title">Есть вопросы?</h4>

                  <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>

                <div class="modal-body">
                  Связаться с поддержкой можно по номеру +7 993 980‑49‑87 в Telegram или WhatsApp.
                  Поддержка работает каждый день с 10 до 21 часа по московскому времени.
                </div>

                <div class="modal-footer justify-content-start gap-2">
                  <a href="https://t.me/+79939804987"
                     target="_blank"
                     class="pp-btn-black btn">Telegram</a>

                  <a href="https://wa.me/79939804987"
                     target="_blank"
                     class="pp-btn-black btn">Whatsapp</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>


    <script src="/static/website/assets/nocdn/bootstrap%405.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="/static/website/assets/scripts/main.js"></script>



  </body>

</html>

"""

print(text_from_html(html))
