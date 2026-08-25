/* Privé Motors — fleet data.
   Single source of truth for the brand strip, the collection grid, and the guided finder.
   Swap `img` for a real transparent cut-out PNG per vehicle when photography is ready —
   keep the same side-profile angle and horizon line across every car so the grid stays consistent. */

const PLACEHOLDER_IMG = 'assets/fleet/placeholder-car.svg';

const BRANDS = [
  'Lamborghini', 'Ferrari', 'Rolls-Royce', 'Bentley', 'Porsche',
  'Mercedes-Benz', 'BMW', 'Audi', 'Chevrolet', 'Tesla', 'Range Rover'
];

/* crest/symbol versions — used on the collection filter row (small, square-ish bounding box) */
const BRAND_LOGOS = {
  'Lamborghini': 'assets/logos/brands/lamborghini.svg',
  'Ferrari': 'assets/logos/brands/ferrari.svg',
  'Rolls-Royce': 'assets/logos/brands/rolls-royce.svg',
  'Bentley': 'assets/logos/brands/bentley.svg',
  'Porsche': 'assets/logos/brands/porsche-crest.svg',
  'Mercedes-Benz': 'assets/logos/brands/mercedes-benz-star.svg',
  'BMW': 'assets/logos/brands/bmw.svg',
  'Audi': 'assets/logos/brands/audi.svg',
  'Chevrolet': 'assets/logos/brands/chevrolet.png',
  'Tesla': 'assets/logos/brands/tesla.svg',
  'Range Rover': 'assets/logos/brands/range-rover.svg',
};

/* wordmark/full-logo overrides for the homepage marquee (no separate text label there,
   so Porsche's lettered logo and Mercedes' full logo-with-wordmark read better than the crest/star alone) */
const BRAND_LOGOS_HOME = { ...BRAND_LOGOS,
  'Porsche': 'assets/logos/brands/porsche-wordmark.svg',
  'Mercedes-Benz': 'assets/logos/brands/mercedes-benz.svg',
};

const OCCASIONS = [
  { id: 'business', label: 'Business' },
  { id: 'wedding', label: 'Wedding' },
  { id: 'weekend', label: 'Weekend' },
  { id: 'drive', label: 'The Drive' },
];

const FLEET = [
  { id:'lamborghini-urus-2023', brand:'Lamborghini', model:'Urus', year:2023,
    category:'suv', seats:4, hp:650, accel:3.6,
    day:2228, week:13370, month:45450,
    occasions:['business','wedding'], badges:['no-deposit','free-delivery'], terrain:['city','desert'], img:'assets/fleet/lamborghini-urus-2023-1500.webp' },

  { id:'lamborghini-urus-performante-2023', brand:'Lamborghini', model:'Urus Performante', year:2023,
    category:'suv', seats:4, hp:666, accel:3.3,
    day:1999, week:12600, month:52500,
    occasions:['drive','weekend'], badges:['no-deposit'], terrain:['city','desert'], img:'assets/fleet/lamborghini-urus-performante-2023-1500.webp' },

  { id:'lamborghini-huracan-spyder-2021', brand:'Lamborghini', model:'Huracán Spyder', year:2021,
    category:'convertible', seats:2, hp:610, accel:3.4,
    day:2582, week:16520, month:45390,
    occasions:['drive','weekend'], badges:['no-deposit','free-delivery'], terrain:['city'], img:'assets/fleet/lamborghini-huracan-spyder-2021-1500.webp' },

  { id:'lamborghini-huracan-evo-2020', brand:'Lamborghini', model:'Huracán Evo', year:2020,
    category:'sports', seats:2, hp:640, accel:2.9,
    day:1815, week:10892, month:37020,
    occasions:['drive'], badges:['no-deposit'], terrain:['city'], img:'assets/fleet/lamborghini-huracan-evo-2020-1500.webp' },

  { id:'ferrari-f8-tributo-spider-2022', brand:'Ferrari', model:'F8 Tributo Spider', year:2022,
    category:'convertible', seats:2, hp:710, accel:2.9,
    day:2156, week:13800, month:48200,
    occasions:['drive','weekend'], badges:['no-deposit','free-delivery'], terrain:['city'], img:'assets/fleet/ferrari-f8-tributo-spider-2022-1500.webp' },

  { id:'ferrari-portofino-m-2023', brand:'Ferrari', model:'Portofino M', year:2023,
    category:'convertible', seats:4, hp:612, accel:3.45,
    day:2025, week:12750, month:44900,
    occasions:['wedding','weekend'], badges:['no-deposit'], terrain:['city'], img:'assets/fleet/ferrari-portofino-m-2023-1500.webp' },

  { id:'rolls-royce-cullinan-2022', brand:'Rolls-Royce', model:'Cullinan', year:2022,
    category:'suv', seats:5, hp:563, accel:5.2,
    day:2672, week:16900, month:58000,
    occasions:['business','wedding'], badges:['free-delivery'], terrain:['city','desert'], img:'assets/fleet/rolls-royce-cullinan-2022-1500.webp' },

  { id:'rolls-royce-ghost-2020', brand:'Rolls-Royce', model:'Ghost', year:2020,
    category:'sedan', seats:5, hp:563, accel:4.8,
    day:1373, week:8700, month:31500,
    occasions:['business','wedding'], badges:['no-deposit','free-delivery'], terrain:['city'], img:'assets/fleet/rolls-royce-ghost-2020-1500.webp' },

  { id:'rolls-royce-wraith-2021', brand:'Rolls-Royce', model:'Wraith', year:2021,
    category:'sports', seats:4, hp:624, accel:4.4,
    day:1800, week:11400, month:40500,
    occasions:['wedding','drive'], badges:['free-delivery'], terrain:['city'], img:'assets/fleet/rolls-royce-wraith-2021-1500.webp' },

  { id:'bentley-continental-gtc-2021', brand:'Bentley', model:'Continental GTC V12', year:2021,
    category:'convertible', seats:4, hp:542, accel:3.7,
    day:1366, week:8620, month:29900,
    occasions:['weekend','wedding'], badges:['no-deposit'], terrain:['city'], img:'assets/fleet/bentley-continental-gtc-2021-1500.webp' },

  { id:'bentley-bentayga-2022', brand:'Bentley', model:'Bentayga', year:2022,
    category:'suv', seats:5, hp:542, accel:4.5,
    day:1550, week:9800, month:34200,
    occasions:['weekend','business'], badges:['no-deposit','free-delivery'], terrain:['city','desert'], img:'assets/fleet/bentley-bentayga-2022-1500.webp' },

  { id:'porsche-911-carrera-gts-2024', brand:'Porsche', model:'911 Carrera GTS', year:2024,
    category:'sports', seats:4, hp:473, accel:3.4,
    day:1530, week:9650, month:33800,
    occasions:['drive','weekend'], badges:['no-deposit'], terrain:['city'], img:'assets/fleet/porsche-911-carrera-gts-2024-1500.webp' },

  { id:'porsche-boxster-718-2023', brand:'Porsche', model:'Boxster 718', year:2023,
    category:'convertible', seats:2, hp:300, accel:4.9,
    day:649, week:4100, month:14200,
    occasions:['drive'], badges:['no-deposit','free-delivery'], terrain:['city'], img:'assets/fleet/porsche-boxster-718-2023-1500.webp' },

  { id:'mercedes-s500-2022', brand:'Mercedes-Benz', model:'S 500', year:2022,
    category:'sedan', seats:5, hp:429, accel:4.9,
    day:780, week:4900, month:17100,
    occasions:['business'], badges:['no-deposit','free-delivery'], terrain:['city'], img:'assets/fleet/mercedes-s500-2022-1500.webp' },

  { id:'mercedes-s450-maybach-2023', brand:'Mercedes-Benz', model:'S 450 Maybach', year:2023,
    category:'sedan', seats:5, hp:362, accel:5.9,
    day:1980, week:12500, month:43600,
    occasions:['business','wedding'], badges:['free-delivery'], terrain:['city'], img:'assets/fleet/mercedes-s450-maybach-2023-1500.webp' },

  { id:'mercedes-g63-amg-2023', brand:'Mercedes-Benz', model:'G 63 AMG', year:2023,
    category:'suv', seats:5, hp:577, accel:4.5,
    day:1600, week:10100, month:35200,
    occasions:['business','weekend'], badges:['no-deposit'], terrain:['city','desert'], img:'assets/fleet/mercedes-g63-amg-2023-1500.webp' },

  { id:'bmw-840i-cabrio-2021', brand:'BMW', model:'840i Cabrio', year:2021,
    category:'convertible', seats:4, hp:335, accel:5.2,
    day:802, week:5050, month:17600,
    occasions:['weekend'], badges:['no-deposit','free-delivery'], terrain:['city'], img:'assets/fleet/bmw-840i-cabrio-2021-1500.webp' },

  { id:'bmw-7-series-2023', brand:'BMW', model:'7 Series', year:2023,
    category:'sedan', seats:5, hp:375, accel:5.3,
    day:1100, week:6950, month:24200,
    occasions:['business'], badges:['no-deposit'], terrain:['city'], img:'assets/fleet/bmw-7-series-2023-1500.webp' },

  { id:'audi-rs6-2022', brand:'Audi', model:'RS6 Avant', year:2022,
    category:'sedan', seats:5, hp:591, accel:3.6,
    day:988, week:6200, month:21700,
    occasions:['business','weekend'], badges:['no-deposit','free-delivery'], terrain:['city'], img:'assets/fleet/audi-rs6-2022-1500.webp' },

  { id:'audi-r8-spyder-2024', brand:'Audi', model:'R8 Spyder', year:2024,
    category:'convertible', seats:2, hp:562, accel:3.4,
    day:1371, week:8650, month:30200,
    occasions:['drive','weekend'], badges:['no-deposit'], terrain:['city'], img:'assets/fleet/audi-r8-spyder-2024-1500.webp' },

  { id:'chevrolet-corvette-2022', brand:'Chevrolet', model:'Corvette Stingray', year:2022,
    category:'sports', seats:2, hp:495, accel:2.9,
    day:720, week:4550, month:15900,
    occasions:['drive'], badges:['no-deposit','free-delivery'], terrain:['city'], img:'assets/fleet/chevrolet-corvette-2022-1500.webp' },

  { id:'tesla-model-x-2023', brand:'Tesla', model:'Model X Plaid', year:2023,
    category:'electric', seats:6, hp:1020, accel:2.5,
    day:1300, week:8200, month:28600,
    occasions:['business','weekend'], badges:['no-deposit','free-delivery'], terrain:['city'], img:'assets/fleet/tesla-model-x-2023-1500.webp' },

  { id:'tesla-model-s-plaid-2023', brand:'Tesla', model:'Model S Plaid', year:2023,
    category:'electric', seats:5, hp:1020, accel:2.1,
    day:1400, week:8850, month:30900,
    occasions:['business','drive'], badges:['no-deposit'], terrain:['city'], img:'assets/fleet/tesla-model-s-plaid-2023-1500.webp' },

  { id:'range-rover-vogue-2023', brand:'Range Rover', model:'Range Rover Vogue', year:2023,
    category:'suv', seats:5, hp:523, accel:4.6,
    day:1400, week:8850, month:30900,
    occasions:['weekend','business'], badges:['no-deposit','free-delivery'], terrain:['city','desert'], img:'assets/fleet/range-rover-vogue-2023-1500.webp' },
];

const BADGE_LABELS = {
  'no-deposit': 'No Deposit',
  'free-delivery': 'Free Delivery',
};
