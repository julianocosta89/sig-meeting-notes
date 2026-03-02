SIG: Technical Committee
Date: 2025-11-05
Duration: 12 minutes
============================================================

## Zoom Recording Transcript

**David Ashpole (dashpole)** 00:36 David, Jack.
**Jack Berg** 00:41 Congratulations on joining the TC.
**David Ashpole (dashpole)** 00:43 Thanks, yeah.
It's exciting.
**Jack Berg** 00:47 How have you been doing?
**David Ashpole (dashpole)** 00:49 Been doing alright.
Yeah, just lots going on.
**Jack Berg** 00:54 Yeah, I feel like, you went on parental leave for a while, and right as you were getting back, I went on parental leave, so I haven't seen you in, like, 6 months.
**David Ashpole (dashpole)** 01:02 Yeah, yeah.
**Reiley** 01:05 Good morning.
**Jack Berg** 01:06 Hi, Riley.
**Reiley** 01:08 Hey, David. Hey, Jack.
**David Ashpole (dashpole)** 01:10 And I saw you at the meeting, and I was like, wow.
**Jack Berg** 01:13 It has been a while.
**David Ashpole (dashpole)** 01:20 It's good, though.
**Jack Berg** 02:27 Gosh.
You're muted.
There you are.
**Joshua MacDonald** 02:48 my live… oh, hi, Jack, nice to see you. I thought I was unmuted already.
Interesting set of four we have here. There's a topic I kind of want to break into, but I won't. It's about metric views.
**Jack Berg** 03:01 Well, there's no agenda, and there's only four of us, and Tigrun said he'd be late, Armin's here, so maybe we can't talk about it today.
**Joshua MacDonald** 03:11 It might come up. It's a little bit premature, but seeing the four of you, or four of us, we all have a position, I'm sure.
Nice to have you back on the 2C, by the way. Yeah, yeah, thanks, Jack. It's good to see you. You were on a vacation when I returned, and I haven't seen you in a while, so nice to see you. Since we have Armin, you know, I feel like I've been neglecting trying to get into the Grafana dashboard.
Because I have, like, at least 3 or 4 identities, and I can't figure out which one I'm supposed to use. You know, I've got…
A GitHub, a Microsoft, a Gmail.
And then I've got the SSO path and the password path, and I, like, every time I get lost. Does anyone know… did you succeed, David, at getting into that dashboard?
**David Ashpole (dashpole)** 04:06 I don't know if I know this dashboard exists. Which dashboard is this?
**Joshua MacDonald** 04:11 It's… there's a daily notice in the OTLC channel, and it gives you a link to a dashboard, and it goes to a Grafana login.
And I know vaguely about this. I was part of setting it up.
At my old company.
I helped press buttons for the guy that was doing it.
**David Ashpole (dashpole)** 04:29 Carter Socha.
**Joshua MacDonald** 04:31 set it up I don't know if he's still involved in OTEL.
I don't know if anyone knows how it's configured, but it still works.
**Armin (Dynatrace)** 04:41 So, so I don't think he is, I think it has been maintained by…
Trask most recently, but it stopped working at some point, and I think we haven't
Set it up to… to work again, and that's why we have resorted to the… to this audit log, that shows the recently opened,
GitHub security advisories, because the volume is so low, it's…
still manageable to just look at these, and we just need to make sure that they get… get closed at some point. But it would still be nice to have the dashboard up again on the long run, because it… if there was any
very old one that… that any… like, every one of us would have overlooked for… for a while, then that would be the place to recover it. But…
Recently, we've just used the audit log instead.
That's the other link that's posted there as well.
**Joshua MacDonald** 05:39 Got it.
**David Ashpole (dashpole)** 05:40 I also failed to get that one to work, but…
**Joshua MacDonald** 05:43 I think that's a more tractable one that I can figure out.
That's my full confession, is that I've failed at both of those links.
**Armin (Dynatrace)** 05:53 I, yeah, I figured you're… In the…
rotation until, like, next year, right? And then, once it's your turn from the.
**Joshua MacDonald** 06:03 Yeah, yeah, then I'll get real…
**Armin (Dynatrace)** 06:05 When I click that audit log link, I get to a, you know, like…
**Joshua MacDonald** 06:10 404, basically, so…
**Armin (Dynatrace)** 06:12 Yeah, you need to be an org owner, and we used to have, like, I think the entirety of the TC and GC in there, and at some point, we decided that it would make sense to reduce scope to a handful of GitHub admins, where we have a set of permanent ones that's, like, I don't know, maybe 5 or 6 people?
Trask is among them, because he's doing all of the integration stuff, it seems.
And then, as part of the TC duty rotation week, we would temporarily grant owner access. So that's what we do in the scope of this handoff.
message, and now it's Bogdan, and I think at the end of the week, he would then, promote
Carlos and Demote himself.
**Joshua MacDonald** 06:59 Got it.
Thank you.
Sure. I'm glad to hear that I don't have powers that I should have.
Cause I knew I didn't have those powers, but that's correct. Alright.
**Jack Berg** 07:14 Well, Bogdan isn't here today, and I think we switched to a rotation, where one person is doing all the sort of TC responsibilities at once, all the rotating ones, and coincidentally, I missed the TC meeting last week, so I was derelict on my duties to run the TC meeting, so I guess I can stand in and do that today.
Not that there's a lot of topics or things that need to be organized, but I see a private topic from Carlos.
If I recall correctly, this meeting is now recorded publicly, right? So.
**Carlos Alberto Cortez** 07:49 break.
**Jack Berg** 07:50 If there's no other topics, can we jump over to the, the private video chat to talk about that?
**David Ashpole (dashpole)** 07:59 Yep.
**Carlos Alberto Cortez** 08:00 Perfect. See you later.
**Jack Berg** 08:01 Alright, see you.
**Armin (Dynatrace)** 08:03 See you!
