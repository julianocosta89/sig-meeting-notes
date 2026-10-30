SIG: Packaging SIG
Date: 2026-10-29
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Denys Sedchenko** 03:33 Hi, Diego, how are you?
**Diego Hurtado (Dash0)** 03:37 Hey, Denise, doing alright. What about you?
**Denys Sedchenko** 03:42 as well.
You have a very interesting background.
**Diego Hurtado (Dash0)** 03:48 The kitchen…
**Denys Sedchenko** 03:49 Yeah.
**Diego Hurtado (Dash0)** 03:51 Oh yeah, it's, Of course, it's AI-generated, right, so… doesn't exist.
Hello, Antoine. Hey, Jack.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 04:08 Hello.
**Diego Hurtado (Dash0)** 04:09 Antoine, you're muted.
**Antoine Toulme (Splunk Inc.)** 04:11 Maybe it does exist, maybe you don't know.
**Diego Hurtado (Dash0)** 04:16 That's, that's always a possibility, I mean…
**Antoine Toulme (Splunk Inc.)** 04:20 Yes, it is.
**Diego Hurtado (Dash0)** 04:21 Oh, man.
Now I feel like I have to find it.
**Antoine Toulme (Splunk Inc.)** 04:26 Yep.
**Diego Hurtado (Dash0)** 04:27 Better travel the world, find this kitchen.
**Denys Sedchenko** 04:31 AI is basically the normal distribution of data, so you probably have the most common kitchen, like, restaurant kitchen in the world.
**Diego Hurtado (Dash0)** 04:41 Right?
Well, if I ever open a restaurant…
**Antoine Toulme (Splunk Inc.)** 04:46 I'm sure you can find this place somewhere in Vegas.
**Diego Hurtado (Dash0)** 04:48 Yeah. If I ever open a restaurant, I'll have this exact same kitchen, and I'll…
**Antoine Toulme (Splunk Inc.)** 04:54 Okay.
**Diego Hurtado (Dash0)** 04:55 In the rip.
Leave the restaurant normal or average, or something.
**Antoine Toulme (Splunk Inc.)** 05:02 Okay, so what are we doing?
**Diego Hurtado (Dash0)** 05:04 Alright.
**Antoine Toulme (Splunk Inc.)** 05:06 What's happening?
I think we're supposed to have some… Let's see, where's the detail?
Alright, so… 29th… Which is fine there.
Anything you'd like to talk about, put an agenda item.
So, maybe we can just give you an update on the discussion that's been happening with the CNCF, around this hosting issue and having access to Cloudflare and whatnot. The latest is that, After a lot of discussions and back and forth with Austin.
It turned out this is a solved problem, according to… the… Linux Foundation CNCF guy we're talking to, who's saying that… Other projects, I've had access to object storage in Cloudflare.
And use a, They use a different type of subdomains, which is probably fine for the use case we have, because we could always alias it to the Packaging subdomain.
And as far as I know, we're still waiting for Cloudflare Access anyway.
Denys, do you have access to anything in Cloudflare more than before?
**Denys Sedchenko** 06:43 No, I don't. And regarding subdomains, like, on Netlify's side, we can just have a redirect, because they mentioned they have, like, a specific subdomain, the CDN.cncl.io. We can just have a subdomain. I checked, like, the Debian and, like, Fedora, they work with redirects fine.
It's not a problem for us, maybe it's even, like, solves some of our… problems related to SSL and etc. I think, like, Metlify should allow, like, to make, I don't know, worker, like, a page that basically does the redirect.
**Antoine Toulme (Splunk Inc.)** 07:15 Dip.
Yeah, alright, so… That's the situation we're in, any comments?
**Denys Sedchenko** 07:26 I have just one comment.
So far, we've been focused on Fedora.
**Antoine Toulme (Splunk Inc.)** 07:32 Hmm.
**Denys Sedchenko** 07:32 But… Regarding elephant in the room, Ubuntu and Debian.
I don't know whether we are going to use, I don't recall the name of the service that Ubuntu actually uses.
**Antoine Toulme (Splunk Inc.)** 07:50 really holy.
**Denys Sedchenko** 07:51 Launchpad. Launchpad.
**Antoine Toulme (Splunk Inc.)** 07:52 But, yeah.
**Denys Sedchenko** 07:54 So, to avoid, like, basically… like… And for Debian, it wouldn't probably work, because they, like.
they serve Ubuntu, so if we have Ubuntu, Fedora, and Debian, we would have, like, free… Platforms where we build packages.
And in order to reduce our burden, I was thinking to return back to OpenSuse OPS and to use it right now to build all the Debian stuff. Maybe eventually I will move the RPM stuff there as well, because account, email account, for making new accounts, I have all of that, so, like, for me, spinning in a… Registering there is quite easy. I could… I would, like, also like to try to make the Debian an Ubuntu part there, at least prototype, as long as we're waiting for… for the Cloudflare and the main part to be done.
**Antoine Toulme (Splunk Inc.)** 08:53 Okay.
No problem there.
Okay.
Yeah, that's where we are, I guess.
Okay, is there anything… any other topics for today?
Besides those.
Because unfortunately, Denise just can say, yes, go for it, and feel free to open an issue if you want, but… I'll just put that in the notes. Denys offering to… work on the Debian Packaging.
Maybe using… propensity.
**Denys Sedchenko** 09:43 OBS, like, corrected.
**Antoine Toulme (Splunk Inc.)** 09:47 Good.
Okay.
**Ted Young (Raintank, Inc. – Grafana Labs)** 09:50 I missed the Cloudflare bit, but is there any poking you need me to do?
Where that it would be helpful for me to do?
**Denys Sedchenko** 09:58 You can escalate, please.
Like, we basically need… Like, the button to actually enable to get access, like.
somehow, someone from OpenTelemetry admins of the Cluster namespace have to enable that feature for us.
**Ted Young (Raintank, Inc. – Grafana Labs)** 10:13 Okay.
**Antoine Toulme (Splunk Inc.)** 10:14 Let me add you to that discussion, Ted.
**Ted Young (Raintank, Inc. – Grafana Labs)** 10:17 Yet.
**Antoine Toulme (Splunk Inc.)** 10:18 Next.
From the beginning, done. Confirm.
This is a weird set of DMs. The last, added to this discussion is, Jeffrey Isika.
Who is telling us that, okay, now, there's a way to do this, do not, do not do anything different than the normal stuff.
They would give us an openteometry.cdn.cncfio.
They're like, okay, you know?
**Ted Young (Raintank, Inc. – Grafana Labs)** 10:49 Okay.
Thanks, I'll take a look at that.
**Antoine Toulme (Splunk Inc.)** 10:52 you.
Yeah, I… I'm not sure how to push, pull, or plead, beg.
I have no idea what's gonna work.
Seems like, patients would work.
But I'm in a different spread where I've been with Jeffrey Sika for over a year.
trying to get them to sign a piece of paper between them and the IBM, so… I am. I'm well used to seeing those things kind of go sideways for a while.
I don't like it. Okay.
**Ted Young (Raintank, Inc. – Grafana Labs)** 11:22 Well, I'll see… see if I can help push on that.
**Antoine Toulme (Splunk Inc.)** 11:27 Thank you.
Okay, just maybe quickly, there's a message on the channel about having something about the demo SIG also looking to do packaging. Have you folks looked at that?
I was just reading that.
Let me find it.
So that's the last message on the chat today, from Jack Schiracy, about an hour ago.
he's asking if there's a central location where packaging is laid out the format to be produced. I think we can say with certainty that's our GitHub repo, right?
**Denys Sedchenko** 12:09 Yeah, we have all of the packaging for Debian RP on there.
**Antoine Toulme (Splunk Inc.)** 12:13 And I'm wondering why he's asking us, but that's fine. And now he sees the community demo SIG appears to be producing work that may have been done here, identifying where the source agents in the hotel best practice have been determined that the operator images are not the best practice.
So he's just pointing out that there's some duplication of work. Does anyone here have any take about this? Or do we… I personally don't have the time to go to the demo SIG and tell them that the ways are wrong and they need to talk to us.
So, just FYI, maybe… Ted, do you know who is the GC or TC for… the community, the Demo SIG, who could, kind of.
**Ted Young (Raintank, Inc. – Grafana Labs)** 12:54 I can look into that. I think it's Severin. Severin would be my guess, but…
**Antoine Toulme (Splunk Inc.)** 12:58 Yeah.
**Ted Young (Raintank, Inc. – Grafana Labs)** 12:59 I'll look into it, yeah.
**Antoine Toulme (Splunk Inc.)** 13:02 Okay, just something to bring up so that we don't duplicate efforts, but… Besides that, I don't mind if the domestic starts to have its own opinions about stuff, but that's not really what we're trying to do here. We're trying to demonstrate maturity by having, you know, packages available at scale for the community, so… I don't know what the Masik wants to do with it.
I haven't seen any discussions on Slack.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:27 Yeah, people have duplicated efforts across a number of places because there was no centralized place for this. I think packaging is still viewed as this, like, emerging source of information, of packages.
And so, like, yeah, I think everybody will sort of get behind it once, once they're aware of it, and, you know, I think it'd be crazy for somebody else to be like, hey, I get that there's packaging out here publishing, you know, images, packages that we could use, but, you know, for this reason, I want to recreate work, I want to do it this way.
That'd be… that'd be a pretty silly argument if somebody made that, so… Yeah, I would guess the demo just isn't aware of what packaging is doing, and, you know, we know what's going on with the operator. The operator has historically published these images because they didn't exist anywhere else, and they're eager to get that off their hands.
**Antoine Toulme (Splunk Inc.)** 14:18 I think that's exactly it. And, Hopefully, we have those discussions at CubeCon too, and maybe that helps.
A little bit, I have no idea.
I mean, I think those things take time anyway, right? We… you… but… Cool.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 14:37 Speaking of which, if anybody wants to review the, the… add another set of eyes to the PR that I opened for publishing Docker images. Mikel reviewed it and pushed a bunch of commits to, like, do additional hardening and, you know, add his own, spice to it. And, so I wouldn't be surprised if he's ready to give it, like, a green checkmark pretty soon, so if you intend on reviewing it.
Should do so.
**Ted Young (Raintank, Inc. – Grafana Labs)** 15:06 Great.
**Antoine Toulme (Splunk Inc.)** 15:07 Good. Thanks, Meet.
I'll just put a note of that in the notes as well. What am I doing?
Oh, I lost my bullet points.
Here we go.
Alright, so you're talking specifically about the… 162.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 15:50 The one.
**Antoine Toulme (Splunk Inc.)** 15:52 one.
This is not my day. I'm making mistakes here.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 15:58 Well, it's still early, so there's time to turn it around.
**Antoine Toulme (Splunk Inc.)** 16:02 Thank you, that's very nice of you to say.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:12 Well, we don't need to belabor this if there's no other topics. Let's, let's give folks some time back, huh?
**Antoine Toulme (Splunk Inc.)** 16:19 Yep, to do. Thank you all.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:21 See ya.
