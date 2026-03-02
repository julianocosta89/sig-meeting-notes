SIG: Developer Experience SIG Meeting
Date: 2025-11-26
Duration: 24 minutes
Zoom Recording URL: https://zoom.us/rec/share/ZM_UBw9YPOvbqPfVX6fIVlzn8p0BkHqh7SQMTDtczYV9iBR8p5Q5_rh4ZVgG9ZGh._5hbdQUsoIx20Pha
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 01:22 Hello, hello.
**tristan** 01:24 I hate.
**Damien Mathieu** 01:26 Good morning.
**Juliano Costa | Datadog** 01:28 Good morning.
How are things?
**Damien Mathieu** 01:36 Good.
**tristan** 01:41 Good. Kid just went back to bed, so I made it.
**Juliano Costa | Datadog** 01:48 Oh, man, I feel that… We are… we are all along the same boat.
So the sixth season started here, so the kid is at home today.
**tristan** 02:03 Oh, yeah.
Jeez.
That's gonna be terrible.
**Juliano Costa | Datadog** 02:08 Yeah.
**tristan** 02:14 Alright, what's the suit you're wearing?
**Juliano Costa | Datadog** 02:16 What? I just, so, inside Daradot, they have, guilds.
This is the… black in tech.
**tristan** 02:27 I know.
**Juliano Costa | Datadog** 02:27 logo.
**tristan** 02:28 I'm not that black, but yeah, I wish I was.
**Juliano Costa | Datadog** 02:32 I grew up playing basketball when I always wanted to be Black.
**tristan** 02:39 Nice. That's cool, Datadog, doesn't it?
**Juliano Costa | Datadog** 02:43 Yeah, and I also have one from, SOMOS, which is the, latin America.
So, it's also nice, it's the dog with a mug, and the smoke coming out of the coffee is the…
the South America map.
**tristan** 03:03 Oh, nice.
Very cool. Pretty cool.
at the… Main things I wanted to discuss today were…
If you've heard from Tim, and then talk about how we… if we can split up the remaining blog posts as well.
**Juliano Costa | Datadog** 03:25 Yeah, I don't know now if we should actually wait anymore, or if… because if we… if we can get approval, or if we start…
Let me rephrase that. If we work on the new blog posts and get approval from the reviewer, I think we should just go. And then we just restructure the beginning, because Mastodon is a small team, and sometimes they take a while to reply. I already pinged team twice.
**tristan** 03:56 Okay.
**Juliano Costa | Datadog** 03:56 I'm already on the… on a spot that I feel that I'm disturbing, you know, like…
Yeah, not sure how, I'll give another week and pink again, but yeah. I already pinked, then I bumped it, and now I'm like, oh, okay, yeah, so…
**tristan** 04:16 Yeah, no, that makes sense.
Okay.
I have.
Sort of started the… Don's one.
And so there's…
them… Brock.
And Atlassian, I think, are the remaining ones?
**Juliano Costa | Datadog** 04:45 Yeah, I think at last year, I have part of the recording from you, Tristan, and then part of the recording with.
**tristan** 04:52 For me, yeah.
**Juliano Costa | Datadog** 04:53 So I could take care of that.
**tristan** 04:56 You wanna do… okay. Yeah, I was hoping to split those, those three up, so I could just do two, and then I guess you can do one.
That'd be good.
I'll get to work on… I'm finishing up the…
that first one, and doing Grok, which shouldn't take too long.
Especially the crack one, but the… Yeah.
I guess we gotta… Like, the next…
Step would be figuring out how this integrates with
blueprints and what the contributor SIG is doing.
Once we clean these up.
**Juliano Costa | Datadog** 05:38 We also have Skyscanner, right?
**tristan** 05:40 Oh, right, skyscater.
So we've got… View.
**Juliano Costa | Datadog** 05:47 Warm.
**tristan** 05:48 Blue.
**Juliano Costa | Datadog** 05:50 Was this only recorded by me, or…
**tristan** 05:54 Might have been.
I think I… this is the one where I had to drop.
**Juliano Costa | Datadog** 06:03 No, it's shared with me, so it's not… Mine. Okay.
**tristan** 06:09 Was it a… The… during the collector sig?
I thought this was the one I had to drop. Oh, wait, no, I guess I was here the whole time. I have notes.
Maybe I had the drop from Atlassian? I don't remember.
Yeah, I did hit the drop Atlassian. That's the one.
And you have nothing.
Yeah.
**Juliano Costa | Datadog** 06:31 So this is the Google Drive from, the Skyscanner one.
**tristan** 06:37 Okay.
**Juliano Costa | Datadog** 06:48 Donyon, would you be able to take care of Skyscanner?
**Damien Mathieu** 06:54 To… ride for post?
**Juliano Costa | Datadog** 06:58 Yeah, or the draft.
**Damien Mathieu** 07:01 Sure, I can look into that this week.
**Juliano Costa | Datadog** 07:06 Cool. So then, Damien would do Skyscanner, I would do the… Jesus.
Atlassian?
**tristan** 07:15 Bless him.
**Juliano Costa | Datadog** 07:16 And then, tristan, you do Grok, and the other one that I never know how to pronounce.
**tristan** 07:24 Yeah, I think it's dance.
**Juliano Costa | Datadog** 07:29 Okay. Cool. Just, on that, I saw your…
Your comment on the… on the discussion about industry verticals?
Do you think… That actually affects the way people deploy collectors?
**tristan** 07:49 I wouldn't… I wouldn't think only in the sense of, like, very particular stuff, like, maybe if they're industrial IoT, they might have collector… agents running on, like, hardware, but, like, they… like a…
devices, but aside from that, I wouldn't expect it to. But then, was it a reply? Said something about, yeah, we should definitely categorize them, like, have what industry it is as a tag and as in the document, but I wouldn't expect them to be, like.
laid out as, like, here are the ones for retail. So if you're in retail, read these ones.
Hmm.
Didn't make sense to me.
**Juliano Costa | Datadog** 08:35 Yeah, I, I… I kind of agree, I think it…
What matters more whenever choosing how to deploy is, like, the size and the load that you get, that you have.
But maybe it has some… some,
Good point there, like, if the company is…
like, if it's an online company, like Atlassian, that has
Virtual traffic and people, like, using their system.
**tristan** 09:13 Hmm.
**Juliano Costa | Datadog** 09:14 The load of telemetry that they get is way bigger than
internal platform, a company that just the users from this specific company.
**tristan** 09:30 unknown.
**Juliano Costa | Datadog** 09:30 Are using the tool, or the observability.
So, yeah, then the load would be different, and if… even if the cluster is, like, as big as the other one, the data that is going through is not,
the same, but yeah, again.
**tristan** 09:50 Yeah.
**Juliano Costa | Datadog** 09:50 This is just me guessing, or whatever.
**tristan** 09:53 Right. Yeah, me too. I'd be curious what… more of what they were thinking and why they came to that decision.
Sounded like they already discussed it, and…
Must have… went through those things, so… Yeah, we gotta find out.
It would certainly be nice to be able to give, sort of.
guide on, like, which one might pertain to you, things like that. A way to step through it and just, like…
No.
this one, without having to read on it first, necessarily, the whole thing. But I don't know necessarily how you would do it, except stuff like size, and…
structure, like… What kind of… System you're running.
But yeah, I don't think… I wouldn't think the type of industry, necessarily.
conveys that.
**Juliano Costa | Datadog** 11:00 Yeah, I'm trying to find on the calendar the end user SIG.
**tristan** 11:06 But I…
**Juliano Costa | Datadog** 11:08 I don't know if they have… something…
Like, that happens every week as us, or if it is…
Like, on-demand, whenever they get customers to talk, or users to talk?
**tristan** 11:26 Yeah, well, they must… Yeah, I think it is like that.
Is there anything in Community Repo?
**Juliano Costa | Datadog** 11:35 Yeah, so that's Thursday.
Yeah, like, Thursday 7pm, I don't think I'll ever be able to make it.
**tristan** 11:45 Oh, yeah.
10PT.
**Juliano Costa | Datadog** 11:49 72… 7 to 8, so… Yeah, every two weeks. So they do have recurring ones.
**tristan** 11:59 Okay.
It's on… yeah, it's 1PM my time, so I can go if we need.
**Juliano Costa | Datadog** 12:08 Yeah, well, I don't know if Dan will ever join this scene.
**tristan** 12:13 Oh, really.
**Juliano Costa | Datadog** 12:13 To discuss, but yeah.
**tristan** 12:16 Right, yeah, we should probably…
**Juliano Costa | Datadog** 12:18 Pop in there.
**tristan** 12:21 Except… I'm sure… Probably not this week, but I guess next week.
Where's the captain?
Dude.
Yeah, I can hop in there next week.
**Juliano Costa | Datadog** 12:52 Hi, Kent.
**tristan** 12:59 Always a kid.
Alright.
**Juliano Costa | Datadog** 13:07 Okay.
**tristan** 13:11 That's… what I wanted to discuss. Do we have… Anything else, or just…
Get to work on these blog posts.
**Juliano Costa | Datadog** 13:19 Yeah, I do have an off-topic question for you, Tristan. Well, maybe Damien, I actually also know. So, we deployed an airline service in the demo.
**tristan** 13:31 Mmm.
**Juliano Costa | Datadog** 13:31 And there is, one of these pens that, returns, response time 101.
That's, redirected, I think. HCP Response 101.
**tristan** 13:46 I'm gonna have to continue.
**Juliano Costa | Datadog** 13:49 Yeah, so, for some reason, the airline instrumentation for that, or the leak series instrumentation for that, is tagging the span as they are.
**tristan** 13:59 Hmm.
**Juliano Costa | Datadog** 14:00 But they spent shouldn't be here.
**tristan** 14:02 Yeah.
**Juliano Costa | Datadog** 14:02 at least from one of the community, users that, he, he sent a PR.
creating a rule on the collector to actually remap the spin from here to OK.
**tristan** 14:18 And I was like, yeah, maybe we should fix on the instrumentation and not on the collector. Yeah.
**Juliano Costa | Datadog** 14:24 And he was like, yeah, but
I think the… the instrumentation is… yeah, so, like, I don't know why it's… it's being tagged as error.
I checked the semantic conventions, and .
**tristan** 14:42 Yeah, definitely.
**Juliano Costa | Datadog** 14:42 specification, there is nothing saying that 101 should be error, but there is, like, context-wide stuff. So, like, if in your programming language, in this… in the context of your scenario, this should be tagged as error, then tagged as error.
But I don't think this is the case, so… How do we…
proceed here? What would be the best way to, kind of…
**tristan** 15:09 Yeah, let me… I was going to check the instrumentation library, because I assume it's a bug in there. It's a…
This is…
Oh, wait. This is live view, isn't it? Since it's WebSocket, do you know? It's Phoenix, I assume, but…
**Juliano Costa | Datadog** 15:26 Yeah,
**tristan** 15:27 I didn't know we had… I don't think we have LiveView instrumentation.
**Juliano Costa | Datadog** 15:34 Okay.
**tristan** 15:35 some thug.
**Juliano Costa | Datadog** 15:36 But I don't think we have any, manual instrumentation on the Elixir service.
**tristan** 15:43 Really?
**Juliano Costa | Datadog** 15:46 Hmm, I can…
**tristan** 15:49 So I wouldn't… so… Let me look at the… wait, where'd it go?
Is there… An exception on this?
Do you know?
**Juliano Costa | Datadog** 16:01 Nope.
**tristan** 16:02 There's no exception?
**Juliano Costa | Datadog** 16:04 Nope.
**tristan** 16:05 -Oh.
I just looked at… The one place that…
Oh, wait, this is in Bandit, okay.
So it's nut… Not in the Phoenix code. Let me check the Bandit instrumentation really quick.
Okay.
**Juliano Costa | Datadog** 16:35 I'm running the demo real quick here. It's just starting.
**tristan** 17:14 I don't see how this could happen, cause there's…
The code, it only says… if there's an exception, it will set the status code.
Or if there's…
If it's greater than 500 or equal to 5… greater or equal to 500. So…
I'll have to dig more, because, yeah, it's not a clear… Clear bug.
Oh, wait, I,
Wait, what's… what's setting an exception? Because I'm looking at the screenshot from Jaeger, and it's a front-end proxy that says it has an error.
**Juliano Costa | Datadog** 17:55 Yeah, but .
**tristan** 18:00 So it's Envoy.
**Juliano Costa | Datadog** 18:05 Give me a second. So, the… the error that we get… so I, I do have,
What's the name?
they spend… The bug log.
**tristan** 18:22 Oh, man.
**Juliano Costa | Datadog** 18:23 So, error is being set to true, and error reason is connection termination.
So it's not… Yeah, I don't know where this…
**tristan** 18:40 What is it?
What… on what span is that?
**Juliano Costa | Datadog** 18:44 Give me a sec, I will just open Jaeger here.
**tristan** 18:48 Okay.
**Juliano Costa | Datadog** 18:49 Like, DUI… Find… Share my screen… Jaeger.
Oh, so… It is on the…
on the FlexDUI front-end proxy, so Envoy.
And here, we only have… the 101. Yeah. So, hmm, that's a… so then the issue is on Envoy.
**tristan** 19:22 Yeah, I guess, yeah, because it's not like something… the…
**Juliano Costa | Datadog** 19:26 Okay.
**tristan** 19:27 OpenTelemetry could set from the server side that would get propagated, so it must be…
something with Envoy and getting a 101 or connection terminated. Maybe it's just the protocol from…
the Bandit… the Elixir Services protocol is… Wonky.
And that causes it to terminate, not, what's the word?
doesn't like how it's terminating the WebSocket connection, so that could be why. So it might just be a bug in the web server.
**Juliano Costa | Datadog** 20:08 Wait, in…
**tristan** 20:10 In band… in the… Influ- the Elixir service. Yeah, and Bandit.
Today, it could be… I can… Ask around about that, too.
**Juliano Costa | Datadog** 20:22 Wait, there's a… what's the warning?
The warning is because of the… The timing?
**tristan** 20:30 Ugh.
**Juliano Costa | Datadog** 20:33 Yeah, so if we minimize everything, we see that it's just, like…
Yes, that's the same.
Let me see the other one… And, yeah.
If I do feature…
Back here, I think I get another pair.
Nope.
Huh, there you go.
Yeah, so the, the warning is…
**tristan** 21:12 Thank you.
**Juliano Costa | Datadog** 21:12 Togskill stuff.
**tristan** 21:14 Yeah.
So yeah, that's… my guess is it's…
the website connection isn't closing cleanly between Envoy and the Elixir service.
**Juliano Costa | Datadog** 21:30 So… Where would you recommend me raising this issue? Envoy, or, Bandit, or in the OpenTelemetry…
**tristan** 21:41 It's probably… It's probably Bandit or Phoenix.
So I think…
Oh, that's probably… it says it's coming from… or no, I mean, it's Bandit that would be returning it, but it could be a live view bug, so…
It's either Phoenix or Bandit, and I can also ask around, see if people have seen this before.
Or it doesn't close cleanly.
Yeah, it'd be nice if there's a way to…
know what… what isn't. I wonder if the… have you looked at the logs for the Elixir service?
**Juliano Costa | Datadog** 22:22 I don't think we actually have logs in place. Let's see…
**tristan** 22:27 Because it might be spitting out a warning or something.
**Juliano Costa | Datadog** 22:29 In the book.
**tristan** 22:30 shutting down…
**Juliano Costa | Datadog** 22:44 So this is actually… Those are the logs.
There's…
**tristan** 22:55 Mmm.
**Juliano Costa | Datadog** 23:01 Not much.
**tristan** 23:03 Yeah, gives it away.
**Juliano Costa | Datadog** 23:10 No air or anything.
**tristan** 23:12 Yeah, okay.
**Juliano Costa | Datadog** 23:13 Yeah, I mean, I have access to the code. I could try to add some logs to…
try to find out. The thing is that…
Adding a lot entry in Elixir is not…
as adding a log entry in any other programming language that I'm familiar with, so…
**tristan** 23:35 Yeah, I will ask the…
**Juliano Costa | Datadog** 23:37 Bandit developers and people that use it to…
**tristan** 23:40 if they've had any issues with the WebSocket implementation.
We'll get this figured out.
**Juliano Costa | Datadog** 23:49 Cool.
**tristan** 23:55 Hmm.
**Juliano Costa | Datadog** 23:57 Thank you.
Okay, so…
Let's get the blog posts out, and… or started. Let's see who comes back to us first.
**tristan** 24:13 Alright.
**Juliano Costa | Datadog** 24:16 Awesome.
**tristan** 24:17 Sounds good.
**Juliano Costa | Datadog** 24:17 You guys next week.
**tristan** 24:19 Alright. Bye.
**Juliano Costa | Datadog** 24:21 Bye.
