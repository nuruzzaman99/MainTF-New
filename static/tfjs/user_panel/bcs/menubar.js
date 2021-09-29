let menuItemsName = ['dashboard', 'services', 'order', 'my_team', 'subscriptions', 'events', 'notifications', 'settings'];
let url = window.location.href;

menuItemsName.forEach((item, index) => {
    if (url.includes(item)) {
        let style = document.createElement('style');
        style.innerHTML = `
        .menubar li:nth-child(${index + 1}) {
            background-color: #182f59;
                    border-radius: 5px;
                    border-bottom: none;
                    position: relative;
        }
        .menubar li:nth-child(${index + 1}) i {
                    color: white;
                    border: 1px solid white;
                }
                .menubar li:nth-child(${index + 1}) a {
                    color: white;
                }
                .menubar li:nth-child(${index + 1})::after {
                    content: '';
                    height: 4px;
                    background-color: white;
                    width: 25px;
                    border-radius: 5px;
                    transform: rotate(90deg);
                    top: 25px;
                    right: 0;
                    position: absolute;
                }
                .menubar li:nth-child(${index}) {
                    border-bottom: none;
                }
        `;
        if (!url.includes(menuItemsName[0])) {
            style.innerHTML += `
        .menubar li:first-child {
            border-top: 1px solid rgba(128, 128, 128, 0.5);
        }
        `;
        }
        document.head.appendChild(style);
    }
});