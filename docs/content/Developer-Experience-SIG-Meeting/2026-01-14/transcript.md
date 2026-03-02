SIG: Developer Experience SIG Meeting
Date: 2026-01-14
Duration: 27 minutes
Zoom Recording URL: https://zoom.us/rec/share/OQGKcIwl5E-sR8lQvGu5IM8qV0xlg76__qFdvAoxDsx08FndUt36a2zDrXTE3qEn.CikHbOlHGkdG9gxD
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:13 Hello, hello?
**tristan** 00:14 Hey, hey.
**Juliano Costa | Datadog** 00:17 Is that a virtual background, or is…
**tristan** 00:20 No, it's.
**Juliano Costa | Datadog** 00:21 You are.
**tristan** 00:22 That's alright.
**Juliano Costa | Datadog** 00:24 Oh. My basement. Is that the… Basement.
**tristan** 00:28 Wait, where are you? You're in somewhere different.
**Juliano Costa | Datadog** 00:31 No, I just, had a nice… Project over holidays, though.
Oh, close.
**tristan** 00:38 Same place?
**Juliano Costa | Datadog** 00:40 Yeah, it's the same place. I bought a sticker…
That you'll put on a wall and looks like wood.
**tristan** 00:46 Oh, nice.
**Juliano Costa | Datadog** 00:48 I enjoyed that.
**tristan** 00:53 Yeah, at least you have walls.
I just have insulation.
**Juliano Costa | Datadog** 00:59 Well, at least you're not cold. Is it? Yeah, well, it's pretty cold. Frizzy over there?
**tristan** 01:05 Oh, jeez, yeah.
**Juliano Costa | Datadog** 01:07 It doesn't get…
**tristan** 01:09 I mean, it… it… It's always below freezing, but it doesn't get, like.
super-duper cold here, I guess, but the snow has been crazy this year.
**Juliano Costa | Datadog** 01:19 Yeah, like, here in Altria, like, I think it was the coldest winter that we.
**tristan** 01:24 Oh, really?
**Juliano Costa | Datadog** 01:25 that I… that I saw, and I'm here for, like, 8 years already? Yeah.
**tristan** 01:30 Oh, wow.
**Juliano Costa | Datadog** 01:31 So, I live close to the city center,
And I don't think I ever saw that much snow in the city center before.
**tristan** 01:42 Yeah, they've had twice as much snow as last year.
And…
**Juliano Costa | Datadog** 01:46 Oh.
**tristan** 01:47 Yeah, and it's a lot.
It's weird. Everybody was telling me how it doesn't snow until, like, December… I mean, January, for real, and then it started snowing in, like, November, and didn't… hasn't melted.
It just keeps piling up.
So I'm reaching, like, as high as I am to shovel it off the driveway.
It's pretty annoying.
Right, Damien.
**Damien Mathieu** 02:15 Hey, good morning.
**tristan** 02:17 Hey.
**Juliano Costa | Datadog** 02:17 more money.
**tristan** 02:20 Help us know where you are.
**Damien Mathieu** 02:23 Sorry?
**tristan** 02:24 Do you get much snow where you are, or none?
**Damien Mathieu** 02:26 No, not, no, no swan at all here.
I mean, we are… yeah, we are pretty soft, but, yeah, a bit northern was snow.
**tristan** 02:38 No.
**Juliano Costa | Datadog** 02:39 I think Paris got snow, and it was, like, catastrophic, chaotic.
**Damien Mathieu** 02:45 Yeah, I mean, yeah, any, like, on the first snowflake, Francis had a stop.
**tristan** 02:52 Oh, yeah. Wow.
**Juliano Costa | Datadog** 02:55 But here, like, Vienna, like, Austria, we get snow often, but the amount of snow that we got this year, like, was insane, and there was…
a bunch of flights canceled in the Vienna airport because of the ice.
Oh, wow. Yeah, it was pretty…
Pretty cold, so to say. As Brazilian, for me, it's always cold, but, like, if it's cold for them, then, like, better not step outside.
**tristan** 03:32 Alright, so… I know we don't have, Pavel and, Nicholas and others.
Today, for this meeting, but the…
I don't know if you guys kept track of the MCP ticket?
The… in community?
about whether MCP server stuff will join the DevEx SIG.
There's definitely…
**Damien Mathieu** 04:04 I mean… Push back.
There's still pushback?
**tristan** 04:08 Yeah.
A bit of it, so it's a mix of, some pushback and just, still some…
questions about the scope and things, like, the most recent one, TED, but there's still unanswered other ones, and there's…
Definitely pushback of saying, Like, I don't think it makes sense.
to put it into existing SIGs, like some people suggest, like, well, shouldn't this… the collector one be in the collector SIG? Because the collector SIG seems to just not have the…
Time for it, so… That wouldn't make sense, because then they just won't…
get the attention it deserves, and the… but does that mean it should be its own SIG, or in this SIG? And…
I mean, I don't know the correct answer to that, but the… Yeah, there's definitely still…
Up in the air of whether to merge it, so…
I don't know if we have thoughts on that, or… Anything to reply to them?
to say… which way we want to go. I replied… my last reply was just, I think.
Along the lines of, yeah, what I just said of… it makes
Probably doesn't make sense for it to be in individual SIGs.
Because they're busy. Whether it should be its own or with DevEx, I'm not positive. The… we were asked if…
we'd welcome it, and I thought it made sense, so yeah, we would, but yep.
They're still… yeah, it still seems to be up in the air.
**Damien Mathieu** 05:43 Yeah, I thought it was a settled question.
**tristan** 05:46 Yeah, I think it… I don't know. It seemed like it was, and then… I think it was…
Lou Miller… was… most recent…
**Juliano Costa | Datadog** 05:56 Yeah, I think she… she brought… she brought up some… some interesting point there, Mila.
But I… to be fair, I don't know, I mean, for…
from the discussions that we had, I think we were pretty comfortable in onboarding the MCP here, and eventually getting some traction on the developer experience.
**tristan** 06:19 Yeah.
**Juliano Costa | Datadog** 06:20 on our SIG as well. But from the…
From the project perspective, then maybe it should be its own thing, because it's…
doing something different than we are. I know that there is some…
gray area in the middle where MCP will help developers' experience somehow, but it…
It wasn't what we were doing before, so…
**tristan** 06:51 Certainly not what we planned for, but the…
**Juliano Costa | Datadog** 06:53 Yeah. That doesn't mean we can't… plans can't change, so… Yeah, exactly, so… I'm good, too.
**tristan** 07:01 Meh.
I think it'll probably end up…
being merged and working out to be part of the DevExSig, but they're… yeah.
I know the… What was I gonna say?
Yeah, he, Pebble's updating the proposal still,
I guess he's gonna share before the afternoon call.
But, yeah, I'm not sure exactly what he's changing. I know there's…
So there… yeah, the other questions were the scope and, like, narrowing it down, but I don't know that it makes sense to narrow it down too much, because it…
it isn't part of an individual's… it's not like it's part of the configuration, or the collector, or the specific SIG, like…
And we're not saying it's gonna be one MCP server that covers everything, it's gonna be, you know, whichever one's…
get developed under the DevExSig. It shouldn't necessarily be restricted to say, well, the DevExSig is only going to work on a
MCP server that affects exactly this part, this component, because it should be more open, I think, what people are interested in working on, but…
Come on.
We gotta give some more pushback, I want, I guess.
If we want to get it merged.
So we can get that blog post out and have, people interested joining us.
**Juliano Costa | Datadog** 08:20 Yeah.
I need to… to do the other one that is with me.
Honestly, I… so I had…
I have the… the draft from… from Mastodon, and I… from our previous discussion on that, I stayed with another one.
I don't remember which one it was, but I have the recording here with me, so I was,
responsible for that, but I didn't, do anything yet, so…
**tristan** 08:56 Yeah, for those, I… I've written a draft of the Donksk one, and I'll post that.
On the… in that… Google Doc,
It's still a little… it's still rough.
I don't like writing prose. The…
But then, so I reached out with my, follow-up questions, and it turns out the guy I'm in contact with there is on maternity leave until, January, like, 19th, so he'll be back soon, but I kind of stalled on that after
got that, found that out, that I wouldn't hear anything for a while.
So I still gotta clean it up. I'll post it anyway, but yeah, gotta be cleaned up. And…
I drew… I'll take a… I'm gonna insert the… I drew…
I think you said you could turn these into actual pictures, because I just drew them by hand, because I can't do on the computer.
I don't know what to use, or…
I mean, I can, but it ends up looking very plain and boring.
So…
**Juliano Costa | Datadog** 10:02 There… there is Lucid, Lucid chart.
that I… I think…
**tristan** 10:13 Good.
**Juliano Costa | Datadog** 10:13 and…
**tristan** 10:14 what I was looking for was something that, you know, had, like, Kubernetes, icon-looking things.
So that's…
**Juliano Costa | Datadog** 10:24 another one.
Why is it?
**tristan** 10:27 And I think the…
**Juliano Costa | Datadog** 10:28 I think it's XColidraw, you can… yeah, X-Colidraw, you can add logos, so…
**tristan** 10:36 Okay.
**Juliano Costa | Datadog** 10:37 It's pretty… Let me show to you one that I have open here.
**tristan** 10:43 Oh, great.
**Juliano Costa | Datadog** 10:43 Da-da-da-da.
Sure.
So this one here, it's like,
I added the Teradoc logo, I added the hotel logo.
**tristan** 10:53 Wow.
**Juliano Costa | Datadog** 10:54 we can add also, like, Kubernetes and all that stuff.
**tristan** 10:58 Nice, ex-Calidram.
**Juliano Costa | Datadog** 11:00 Yeah, I'll share the link with you.
**tristan** 11:09 Look at that.
Yeah, I still don't get why there's not… Because I think…
the docs? Wait, I'm either… no, wait. Kubernetes docs, I think, use…
Mermaid? But they don't have, like, a… Way to just… Generate with the logos.
Nice looking curry.
Graphs for some reason.
**Juliano Costa | Datadog** 11:32 Mermaid, uses… there is a…
Where is the docs from Mermaid?
They have… Some integration with…
What is it that… what is it called?
Oh, Jesus, I forgot. Let me see if I can find a, Example here, one sec.
But you can add icons. For instance, for Java, there is the Java icon.
So I don't know… I don't remember from where those icons are coming from.
**tristan** 12:15 Yeah, there doesn't seem to be just, like, a repo…
**Juliano Costa | Datadog** 12:19 Like, import icons.
I… I know that you can't… Yeah
Let me… do we have a search? Yes.
Gavana… let's see.
Nope.
**tristan** 12:40 I tried just asking… an AI to do it, and it was crap, so… Whatever.
Maybe Claude Code could do it, but I don't have to.
**Juliano Costa | Datadog** 13:00 I… I don't… I don't remember where this is. I'll try to find and…
**tristan** 13:05 Super Mermaid?
**Juliano Costa | Datadog** 13:06 Yeah, async.
**tristan** 13:09 Alright.
Sure.
**Juliano Costa | Datadog** 13:11 But I, I remember, I remember having the, the logo.
**tristan** 13:15 I just don't remember from where the log came from.
**Juliano Costa | Datadog** 13:19 And I know that they have some limitations, so, like…
they were using a library, something that is not from Mermaid.
And you could only use whatever was there, so if there was no Kubernetes logo, then you couldn't add a…
**tristan** 13:37 Yeah.
**Juliano Costa | Datadog** 13:38 as well.
Something like that.
**tristan** 13:40 Yeah, I also tried using this… Python diagrams library that does have Kubernetes things?
**Juliano Costa | Datadog** 13:48 Okay.
**tristan** 13:49 And I asked it to… but it doesn't support sidecars. Like, you can't just,
you can't visualize a sidecar, and that was, like, one of the important things to show in the… in the, like, three diagrams I have. Okay, mermaid icons.
So I got pre-upset, and it was funny, because Claude, not Claude, I don't know, whatever thing I used.
did generate.
The AI did generate a sidecarb.
Based diagram, but it just hallucinated it, so it didn't actually compile.
But… So, pretty frustrated with diagramming right now. Okay, I'll look at these.
**Juliano Costa | Datadog** 14:27 So there is one, like, simple here, like, image shape.
That seems to be, like, custom? Not sure. Let me… let me see on the online flow how that will look like on the…
Oh, yeah, cool. So, basically, you can add a SVG, as you like, so…
**tristan** 14:54 to.
**Juliano Costa | Datadog** 14:55 Let me… let me share here again.
So… here's how they are doing.
And I just passed a… the path for the SVG.
So maybe we can upload to our repo, and then just, use whatever.
**tristan** 15:15 Fantastic.
**Juliano Costa | Datadog** 15:16 Yep.
**tristan** 15:18 Okay.
Cool.
**Juliano Costa | Datadog** 15:22 Cool, yeah, this one is new, I didn't know about that. What I was trying to find is this. So, like, here they… there is this FA…
User?
FA is Font Awesome.
**tristan** 15:38 I remember.
**Juliano Costa | Datadog** 15:40 Awesome. And I think Phone Awesome… so, like, Mermaid Support 2 version whatever?
And then there is, like…
Let's see if we have Kubernetes.
Yeah, no… no icons for Kubernetes, so even if they supported the latest, we wouldn't be able to use…
**tristan** 16:06 Yeah.
**Juliano Costa | Datadog** 16:10 So I know because I use the Java one… yeah, this one.
**tristan** 16:14 Yeah.
**Juliano Costa | Datadog** 16:16 Yep,
Where do I stop sharing? There you go.
**tristan** 16:24 Alright. Yeah, but the SVG thing solves a lot, because then we can simply use…
**Juliano Costa | Datadog** 16:32 Whatever we want.
**tristan** 16:34 Yeah, perfect, that'll probably work.
**Juliano Costa | Datadog** 16:37 And we can keep the… the configurate… the…
configuration as code. If we do is call it raw, then we need to…
To draw it, and then, like…
I think ScullyDraw only allows you to save the… the drawing.
If you have an account or something… let me see…
**tristan** 17:08 Okay, yeah, and then Kubernetes has an icon set.
I just put that in the chat.
the… so then I just referenced those.
Can't… still can't visualize a sidecar, but I'll just make that up.
**Juliano Costa | Datadog** 17:33 I, I, I think, I think I'm too… too picky. I, I, I, I can't, like, can't they?
decrease the font size, like, 1 millimeter here to not have, like, the letter together with the border, like, come on, guys.
**tristan** 17:50 Yeah, Chris.
**Juliano Costa | Datadog** 17:53 Like they did with Contraplane.
**tristan** 17:55 Oh, yeah.
**Juliano Costa | Datadog** 17:55 with kproxy and Kubelet, like…
**tristan** 17:58 Please. Yep.
**Juliano Costa | Datadog** 18:00 Yup. Week.
Anyways, yeah, this is just me, big picky.
My brother works with marketing, and he likes
he… I grew… he's 10 years older than me, so I grew up with him playing with Photoshop and Carl Draw and that stuff, so I'm, like…
I'm too detail-oriented, so to say, when it comes to visualization.
**tristan** 18:32 Yeah.
**Juliano Costa | Datadog** 18:41 okay, so that… that helps a bunch. The… the thing here on the… On the icons from…
From… Yeah, there you go. There is another folder where you have all the SVG.
**tristan** 18:59 Okay, yep.
**Juliano Costa | Datadog** 19:01 So, that would help, because then we can simply
as the SVG to the flowchart.
Let me see…
didn't actually work, I don't know why.
So, I added the GitHub, blob.
icon, and it didn't render, so I don't know…
**tristan** 20:08 Okay.
**Juliano Costa | Datadog** 20:09 If that will actually work.
Yeah, interesting.
**tristan** 20:13 I'll figure it out.
It's… I don't know how Brett Hook. Lori? The other one you were saying?
**Juliano Costa | Datadog** 20:58 Which one? What?
**tristan** 21:00 I feel like you…
mentioned this tool a second ago. But yeah, it would be better if we could do it in code.
Provided.
Ran into this.
**Juliano Costa | Datadog** 21:08 I have… I've never seen this.
**tristan** 21:11 Oh, okay.
**Juliano Costa | Datadog** 21:14 The other one was Excalibra.
**tristan** 21:16 No, no, yeah.
**Juliano Costa | Datadog** 21:18 Yeah, I was,
I was saying… I was saying… Jesus, I was telling that, we… we wouldn't be able to… to save and modify, but we are, even without logging in, so no account needed or anything, which is…
Good. So, like, you save the project as a .excolidraw file, and then whenever you open Excolidraw, you just open it?
**tristan** 21:43 Oh, nice.
**Juliano Costa | Datadog** 21:44 So, this is… This is cool if we can't make mermaid work.
**tristan** 21:51 Yeah, but Merid should work, so…
**Juliano Costa | Datadog** 21:54 Yep.
And I also saw on Mermaid Docs that you can also use a PNG file, so…
**tristan** 22:01 Okay, beautiful.
**Juliano Costa | Datadog** 22:03 No need to be the…
**tristan** 22:12 Okay.
Owen.
I don't know if… You all saw that the Grok is now kind of NVIDIA?
So, I don't know exactly how that blog post is gonna go, but…
I assume we'll still just write it as groc, but I gotta…
**Damien Mathieu** 22:46 They've been acquired.
**tristan** 22:48 Sort of.
It's sort of like an acquisition to get around,
what's it called, Monopoly claims, so they didn't technically acquire it, but everybody I know that works there is now working at NVIDIA.
And so, like, all the technology we're talking about is now at NVIDIA.
They, they, they exclude, I think exclusively license their technology.
And then Aqua hired everybody?
So technically, Grok still exists, and they didn't acquire it, but they acquired it.
Bro.
Intents and purposes, just not legally.
that way they're not… stopped by antitrust.
So yeah, that could get interesting, but…
I don't know. Should be fine. But yeah, it might turn into an NVIDIA post, so we'll see.
**Juliano Costa | Datadog** 23:41 That means that you could be a millionaire.
**tristan** 23:46 No.
Because I left.
**Juliano Costa | Datadog** 23:49 Yeah, yeah, yeah, but I… you… you… could have.
**tristan** 23:52 Yeah, yeah, no, I thought about that.
That happened to me one.
**Juliano Costa | Datadog** 23:58 I mean.
**tristan** 23:58 word.
So…
**Juliano Costa | Datadog** 24:00 Oh, really?
**tristan** 24:01 Yeah, I… I interviewed at WhatsApp.
Before they got acquired by Facebook.
But they didn't… but then they decided, they're like, Because I wouldn't move.
to the Bay Area.
So they were like, we're not looking to hire… Remote right now, so… Wolf.
Then when my wife was still in school.
And she didn't want to move.
So I was like, nope, can't do it, so…
Then they got acquired for, what, $5 billion or something?
**Juliano Costa | Datadog** 24:34 Ugh.
I mean, I don't know if being millionaire is a good thing, but, like, yeah.
**tristan** 24:39 It's better than that.
**Juliano Costa | Datadog** 24:43 I wouldn't mind doing that.
**tristan** 24:44 Oh, yeah.
**Juliano Costa | Datadog** 24:47 Regarding… Regarding the… the… the things that we were doing here.
**tristan** 24:53 Yep.
**Juliano Costa | Datadog** 24:54 I… I found out why it wasn't working, the image. So, the thing is, you need to add the raw link, so, like, the raw.gitub user content. Yeah, yeah, instead of the…
The link to the image.
**tristan** 25:12 Gotcha. The raw works.
Alright, good.
**Juliano Costa | Datadog** 25:17 Cool.
**tristan** 25:17 I'll work on that.
**Juliano Costa | Datadog** 25:18 Cool.
**tristan** 25:19 But…
**Juliano Costa | Datadog** 25:19 If, if you want also to put,
I honestly like playing with Mermaid.
If you want to put the, the image on the, on the draft, and I could take care of, of playing around.
**tristan** 25:35 Boop.
Yeah, I'll do that today. The…
I guess one other thing, unless we have more on… on those, was… did anybody look at the skills thing that,
Nicholas posted about whether… I think it should be MCP servers or skills agent.
I don't fully understand it yet, but it did look interesting of the question of which one we should do. So yeah, figured I'd bring that up if anybody had any thoughts, but…
**Juliano Costa | Datadog** 26:09 I… I haven't…
**tristan** 26:13 Yeah, I haven't dug into it yet.
I pulled it up.
**Juliano Costa | Datadog** 26:20 Yeah, like, this week is my first full week of work. Yeah.
Last week, I worked 3 days, so this is, like…
I still have a bunch to catch up.
**tristan** 26:31 Catch up on. Alright.
Yeah, it looks like a bunch of markdown telling it what to do. I'm still surprised at how much markdown this stuff is, but
Whatever works.
We'll see.
Alright.
is there anything else we should discuss right now, then?
I'll get those… Images cut up and posted.
And the blood clues.
Okay.
Alright.
I'm gonna try to make…
**Juliano Costa | Datadog** 27:10 the…
**tristan** 27:11 later meeting, which will, I guess, be discussing the community PR more, and the skills versus MCP server.
Hopefully get some resolution there and move forward, get a blog post out about MCP Server.
Soon.
Alright.
**Juliano Costa | Datadog** 27:32 Wolf.
**tristan** 27:32 Boop.
**Juliano Costa | Datadog** 27:33 Nope.
**tristan** 27:34 Thanks, everyone.
But…
**Juliano Costa | Datadog** 27:36 Yep.
