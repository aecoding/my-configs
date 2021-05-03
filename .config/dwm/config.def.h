/* See LICENSE file for copyright and license details. */

/* appearance */
static const unsigned int borderpx  = 1;        /* border pixel of windows */
static const unsigned int gappx     = 0;        /* gaps between windows */
static const unsigned int snap      = 24;       /* snap pixel */
static const unsigned int systraypinning = 0;   /* 0: sloppy systray follows selected monitor, >0: pin systray to monitor X */
static const unsigned int systrayspacing = 2;   /* systray spacing */
static const int systraypinningfailfirst = 1;   /* 1: if pinning fails, display systray on the first monitor, False: display systray on the last monitor*/
static const int showsystray        = 1;     /* 0 means no systray */
static const int showbar            = 0;        /* 0 means no bar */
static const int topbar             = 1;        /* 0 means bottom bar */
static const char *fonts[]          = { "monospace:size=10" };
static const char dmenufont[]       = "monospace:size=10";
static const char col_gray1[]       = "#222222";
static const char col_gray2[]       = "#161d6f";
static const char col_gray3[]       = "#bbbbbb";
static const char col_gray4[]       = "#eeeeee";
static const char col_cyan[]        = "#f6f6f6";
static const char *colors[][3]      = {
	/*               fg         bg         border   */
	[SchemeNorm] = { col_gray3, col_gray1, col_gray2 },
	[SchemeSel]  = { col_gray4, col_cyan,  col_cyan  },
};

static const char *const autostart[] = {
	"st", NULL,
  "autostart", "&", NULL,
	NULL /* terminate */
};
/* tagging */
static const char *tags[] = { "a", "s", "d", "f", "h", "j", "k", "l" };
static const char *tagsalt[] = { "a", "s", "d", "f", "h", "j", "k", "l" };

static const Rule rules[] = {
	/* xprop(1):
	 *	WM_CLASS(STRING) = instance, class
	 *	WM_NAME(STRING) = title
	 */
	/* class      instance    title       tags mask     isfloating   monitor */
	{ "Gimp",     NULL,       NULL,       0,            1,           -1 },
	{ "Firefox",  NULL,       NULL,       1 << 8,       0,           -1 },
};

/* layout(s) */
static const float mfact     = 0.55; /* factor of master area size [0.05..0.95] */
static const int nmaster     = 1;    /* number of clients in master area */
static const int resizehints = 0;    /* 1 means respect size hints in tiled resizals */

static const Layout layouts[] = {
	/* symbol     arrange function */
	{ "[]=",      tile },    /* first entry is default */
	{ "[M]",      monocle },
	{ "><>",      NULL },    /* no layout function means floating behavior */
};

/* key definitions */
#define MODKEY Mod3Mask
#define TAGKEYS(KEY,TAG) \
	{ MODKEY,                       KEY,      view,           {.ui = 1 << TAG} }, \
	{ Mod4Mask,             KEY,      tag,            {.ui = 1 << TAG} }, \
	/*{ MODKEY|ControlMask,           KEY,      toggleview,     {.ui = 1 << TAG} }, \
	{ MODKEY|ControlMask|ShiftMask, KEY,      toggletag,      {.ui = 1 << TAG} },*/

/* helper for spawning shell commands in the pre dwm-5.0 fashion */
#define SHCMD(cmd) { .v = (const char*[]){ "/bin/sh", "-c", cmd, NULL } }

/* commands */
static char dmenumon[2] = "0"; /* component of dmenucmd, manipulated in spawn() */
static const char *dmenucmd[] = { "dmenu_run", "-m", dmenumon, "-fn", dmenufont, "-nb", col_gray1, "-nf", col_gray3, "-sb", col_cyan, "-sf", col_gray4, NULL };
static const char *termcmd[]  = { "st", NULL };
static const char *termcmd2[] = { "alacritty", NULL };
static const char *volup[] = { "volume", "up", NULL};
static const char *voldw[] = { "volume", "down", NULL};
static const char *layout[] = { "layout", NULL};
static const char *qutebrowser[] = { "qutebrowser", NULL };
static const char *browser[] = { "brave", NULL };
static const char *pomodoro[] = { "pomoStart", NULL };
static const char *vimwiki[] = { "st", "-e", "nvim ~/.vimwiki/index.wiki", NULL };
static const char *n[] = { "st", "-e", "nnn", NULL };
static const char *notifya[] = { "notifyGroup", "a", NULL};
static const char *notifys[] = { "notifyGroup", "s", NULL};
static const char *notifyd[] = { "notifyGroup", "d", NULL};
static const char *notifyf[] = { "notifyGroup", "f", NULL};
static const char *notifyh[] = { "notifyGroup", "h", NULL};
static const char *notifyj[] = { "notifyGroup", "j", NULL};
static const char *notifyk[] = { "notifyGroup", "k", NULL};
static const char *notifyl[] = { "notifyGroup", "l", NULL};

static Key keys[] = {
	/* modifier                     key        function        argument */
	{ MODKEY|ControlMask,           XK_d,      spawn,          {.v = dmenucmd } },
	{ MODKEY,                       XK_t,      spawn,          {.v = termcmd } },
	{ Mod4Mask,                     XK_t,      spawn,          {.v = termcmd2 } },
	{ MODKEY|ShiftMask,             XK_u,      spawn,          {.v = volup } },
	{ MODKEY|ShiftMask,             XK_d,      spawn,          {.v = voldw } },
	{ MODKEY,                       XK_e,      spawn,          {.v = layout } },
	{ MODKEY|ShiftMask,             XK_p,      spawn,          {.v = pomodoro } },
	{ MODKEY,                       XK_q,      spawn,          {.v = qutebrowser } },
	{ MODKEY,                       XK_w,      spawn,          {.v = browser } },
	{ MODKEY,                       XK_v,      spawn,          {.v = vimwiki } },
	{ Mod4Mask,                     XK_n,      spawn,          {.v = n } },
  { MODKEY|ControlMask,           XK_space,  focusmaster,    {0} },
	{ MODKEY|ShiftMask,             XK_b,      togglebar,      {0} },
	{ MODKEY,                       XK_n,      focusstack,     {.i = +1 } },
	{ MODKEY,                       XK_p,      focusstack,     {.i = -1 } },
	{ MODKEY|ShiftMask,             XK_h,      setmfact,       {.f = -0.05} },
	{ MODKEY|ShiftMask,             XK_l,      setmfact,       {.f = +0.05} },
  { MODKEY,                       XK_n,      togglealttag,   {0} },
	{ MODKEY|ShiftMask,             XK_t,      zoom,           {0} },
	{ MODKEY,                       XK_b,      view,           {0} },
	{ MODKEY,                       XK_c,      killclient,     {0} },
	{ MODKEY|ShiftMask,             XK_0,      setlayout,      {.v = &layouts[0]} },
	{ MODKEY|ShiftMask,             XK_1,      setlayout,      {.v = &layouts[1]} },
	{ MODKEY|ShiftMask,             XK_2,      setlayout,      {.v = &layouts[2]} },
	{ MODKEY|ShiftMask,             XK_3,      setlayout,      {.v = &layouts[3]} },
	{ MODKEY|ShiftMask,             XK_4,      setlayout,      {.v = &layouts[4]} },
	{ MODKEY,                       XK_space,  setlayout,      {0} },
	{ MODKEY|ShiftMask,             XK_space,  togglefloating, {0} },
	{ MODKEY,                       XK_0,      view,           {.ui = ~0 } },
	{ MODKEY|ShiftMask,             XK_0,      tag,            {.ui = ~0 } },
	{ MODKEY,                       XK_comma,  focusmon,       {.i = -1 } },
	{ MODKEY,                       XK_period, focusmon,       {.i = +1 } },
	{ MODKEY|ShiftMask,             XK_comma,  tagmon,         {.i = -1 } },
	{ MODKEY|ShiftMask,             XK_period, tagmon,         {.i = +1 } },
	{ MODKEY,                       XK_a,      spawn,          {.v = notifya } },
	{ MODKEY,                       XK_s,      spawn,          {.v = notifys } },
	{ MODKEY,                       XK_d,      spawn,          {.v = notifyd } },
	{ MODKEY,                       XK_f,      spawn,          {.v = notifyf } },
	{ MODKEY,                       XK_h,      spawn,          {.v = notifyh } },
	{ MODKEY,                       XK_j,      spawn,          {.v = notifyj } },
	{ MODKEY,                       XK_k,      spawn,          {.v = notifyk } },
	{ MODKEY,                       XK_l,      spawn,          {.v = notifyl } },
	TAGKEYS(                        XK_a,                      0)
	TAGKEYS(                        XK_s,                      1)
	TAGKEYS(                        XK_d,                      2)
	TAGKEYS(                        XK_f,                      3)
	TAGKEYS(                        XK_h,                      4)
	TAGKEYS(                        XK_j,                      5)
	TAGKEYS(                        XK_k,                      6)
	TAGKEYS(                        XK_l,                      7)
	{ MODKEY|ShiftMask,             XK_q,      quit,           {0} },
};


/* button definitions */
/* click can be ClkTagBar, ClkLtSymbol, ClkStatusText, ClkWinTitle, ClkClientWin, or ClkRootWin */
static Button buttons[] = {
	/* click                event mask      button          function        argument */
	{ ClkLtSymbol,          0,              Button1,        setlayout,      {0} },
	{ ClkLtSymbol,          0,              Button3,        setlayout,      {.v = &layouts[2]} },
	{ ClkWinTitle,          0,              Button2,        zoom,           {0} },
	{ ClkStatusText,        0,              Button2,        spawn,          {.v = termcmd } },
	{ ClkClientWin,         MODKEY,         Button1,        movemouse,      {0} },
	{ ClkClientWin,         MODKEY,         Button2,        togglefloating, {0} },
	{ ClkClientWin,         MODKEY,         Button3,        resizemouse,    {0} },
	{ ClkTagBar,            0,              Button1,        view,           {0} },
	{ ClkTagBar,            0,              Button3,        toggleview,     {0} },
	{ ClkTagBar,            MODKEY,         Button1,        tag,            {0} },
	{ ClkTagBar,            MODKEY,         Button3,        toggletag,      {0} },
};

