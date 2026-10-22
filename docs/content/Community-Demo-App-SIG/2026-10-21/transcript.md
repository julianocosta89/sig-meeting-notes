SIG: Community Demo App SIG
Date: 2026-10-21
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Tobias Oka** 00:44 That's not right.
**Shenoy Pratik** 00:47 What are you doing?
**Tobias Oka** 00:49 Doing great, how are you?
**Shenoy Pratik** 00:51 Okay, good outside.
I started looking into your PR yesterday.
We look good, to be honest.
It's just a matter of time for me to review it.
I just am trying to remember, we are only replacing how we consume the SDK in those PRs, right? That's the I think.
Yup. Yeah. Yeah. I tested the first one out.
Oh.
Yeah, and that worked for me.
I don't… see anything blocking on it. I'll just take a look today.
For both of them.
It's only that we have better control on options, and then when we deploy it in Helm or Kubernetes, it's easy.
**Tobias Oka** 01:40 Exactly, exactly, and so there will be…
**Shenoy Pratik** 01:42 Okay.
**Tobias Oka** 01:43 I wanted to say two more PRs coming.
But it's probably only one. I wanted to do that for a… for… for a Python service as well.
But we did some changes on the repo lately, so I need to actually look at what is actually, like, a good example of Python. Basically, the idea is That for… and we discussed this in another, like, another week, some weeks ago, that, like, the idea is that for all the languages, we have one service where we demonstrate how the operator can basically inject the SDK at runtime, and that way you, with one flip of a configuration, you can just change the… change the SDK version without having to rebuild anything.
**Shenoy Pratik** 02:36 Yeah.
So, will it be… An environment config, or… Something else that'll fill up, but…
**Tobias Oka** 02:47 It will just be whatever you tell the operator, right? So, it will be in the Helm chart of the operator, you tell it.
Like, which workloads it should instrument, and which version it should instrument it with, and stuff like that.
**Shenoy Pratik** 03:02 Okay.
Just trying to see if there's something else that we might need to consider for it.
Thing that should be good.
Would be good, yeah.
**Tobias Oka** 03:22 By the way, regarding this thing that we talked of some weeks ago about this, chain meter, yeah, I… you know, what is the right… what is the right way in Spring Boot to…
**Shenoy Pratik** 03:39 Oh, for the micrometer thing.
**Tobias Oka** 03:40 Sorry, not Shermit.
**Shenoy Pratik** 03:41 Yay!
**Tobias Oka** 03:42 I don't really… I don't… I'm not… I'm not deep enough in it that I can…
**Shenoy Pratik** 03:46 Yeah, yeah.
**Tobias Oka** 03:47 Luke was looking at it, and I thought, okay, rather than saying something nonsensical, I'd rather say nothing.
**Shenoy Pratik** 03:54 Yeah, yeah, even… I'm not that experienced, so what we did was we went ahead and asked the Java and, Java SIG group.
And they mentioned to use whatever we recommend in our docs, rather than micrometer. So, in OpenTelemetry, we have that starter pack for Spring Boot. So, yeah, that's what we ended up doing here.
Yeah, it's just good to have opinions, and people who created it will have the highest opinion interviews, so we went there to ask about it. That's the good part about Demo. You can just ask the other SIGs on what they want to be presented to the world, so… Yeah, we did that. It worked out.
**Tobias Oka** 04:36 Nice.
**Shenoy Pratik** 04:37 Okay, I'm just adding in your PRs in, the notes.
So that other maintainers and approvers also Keep it in their backlog.
**Tobias Oka** 04:48 No.
**Shenoy Pratik** 04:49 Just give me a second… These are the small ones.
This one is 4143.
**Tobias Oka** 05:14 So there are, at the moment, 1, 2, 3. Let me quickly check which ones… You're… 415…
**Shenoy Pratik** 05:26 I think 1… 4149 is not that highlight.
**Tobias Oka** 05:28 Yeah, 4.9 exactly, yeah.
**Shenoy Pratik** 05:32 Mr. Turtle, okay.
Yep, yep.
I'm looking at yesterday and…
**Tobias Oka** 05:40 You do one for accounting, sorry, yeah.
**Shenoy Pratik** 05:43 Yeah.
Okay, accounting as well…
**Tobias Oka** 05:49 Though there, I still have a bit of work, so there I still have some work to do, because I want to make sure that I am not… Making anything worse than before. I guess the front end was a bit tricky.
But yeah, I described it in the… described it in the PL description.
**Shenoy Pratik** 06:10 Why was the front-end tricky?
Because of the JS part?
**Tobias Oka** 06:15 Yeah, because there's the web… because there's the browser part and the backend part, and when I used the automatically injected version, then the test suit became a lot, a lot slower, because it was reinstantiating it every single time, and…
**Shenoy Pratik** 06:31 Oh, yeah.
**Tobias Oka** 06:33 Yeah, but fortunately, Claude is there to… to help. It has a really good understanding, and it helped figure out and work around. Yeah, yeah, yeah.
**Shenoy Pratik** 06:42 It remembers all the issues in the SDK as well, so…
**Tobias Oka** 06:45 Yes, it's crazy, you know? Like, that's the thing, right? Like.
Sometimes it does really stupid things, but many times it knows just so much more than we do.
**Shenoy Pratik** 06:57 Yeah.
**Tobias Oka** 07:00 Yeah.
**Shenoy Pratik** 07:01 The problem is the difference is stark, and you don't know, in the current session, which way is it going.
**Tobias Oka** 07:07 Exactly, exactly. You don't know, will it do a good job or not, and that's… so I had… I had the code lying around for many, many days already, but I just needed to find some time to focus, to look at the PR, because I don't want to submit something that is crap, yeah.
Boom.
**Shenoy Pratik** 07:34 I added every… all the 3PRs in notes, and that should be taken care of.
**Tobias Oka** 07:39 Yeah.
**Shenoy Pratik** 07:40 Yeah, I myself had some open peers, just, like, some quality of life improvements.
like, change log, being checked or not, some CI checks, and all those pieces. Let me move it to draft as well, out of draft. Okay.
And then we should be fine.
What else, what else? There is one… from docker components, IPv6, Mmm, locust flag, looks like there's no easy CLA done.
Oh, my God.
Okay, let me check it out in a breath.
That makes sense. For the operator changes, apart from the one that is pending, do you see any other scope of improvement that we can do that can help the maintenance of the project?
I'm just trying to see… because these are, like, low-hanging fruits, but they're so niche that not everyone will catch it.
**Tobias Oka** 08:44 Yeah, I mean, I saw… so, during my testing, I had the Grafana container run out of getting OOM killed multiple times, to be honest, which was very annoying.
**Shenoy Pratik** 08:57 Yeah, I saw that in some, PRs as well, like, people were trying to contribute some dashboards, and they were not able to spin up in Podman, like, I think Donald mentioned. Are you using Podman or some other container runtime like that?
**Tobias Oka** 09:12 I am using Holima.
**Shenoy Pratik** 09:14 Colima.
**Tobias Oka** 09:15 Yeah.
**Shenoy Pratik** 09:16 Yeah, I'm not sure if it is, like, a non-native Docker thing that Grafana images have a problem with.
**Tobias Oka** 09:23 Oh, dear.
I mean… So, yeah, it's just that our company didn't want to pay Docker licenses anymore, so…
**Shenoy Pratik** 09:33 Yeah, I think no company wants to wait. Even I had to fight a bit to get it, because I cannot approve PRs, even test PRs easily without that. Like, if something fails on Colema, I cannot block a PR saying it fails on Colema.
I was using Kolyma, by the way, yeah.
Anyways, to get it somehow.
**Tobias Oka** 09:56 No.
**Shenoy Pratik** 09:57 AWS also has its own version called Finch, and… something that is open source that is widely used. It works most of the time, but some of the niche images inside the demo, they sometimes give up.
Like, the Grafana and the dimension. Did you try increasing the memory for Grafana? That should have worked.
**Tobias Oka** 10:19 Yeah, I did… I did try that, and it did also work, but I didn't… like, it was not on my… like, I first wanted to finish what I'm doing, I thought maybe it might be worth… Just… Making the limit a bit higher?
So that it works more… is more robust for everyone.
Yeah, and I completely forgot about it until you asked if there's something that I think would be, like, a broader improvement, and I think this would be one.
And…
**Shenoy Pratik** 10:50 Like, one follow-up part on it is, for Grafana, we're thinking of removing it and having Percy's in. There was already a contribution for it. The blocker there was Percy's was not supporting exemplars at that time.
So I remember Juliano went ahead and also contributed to Percy's, those functionalities.
Yes, he… he wanted it to be in. So, I think we were just waiting for his PRs to be merged, and a release to be released out from the proceeds folks. That is in, we might have a very cheap light container for dashboards coming in soon.
That works for Jaeger, Prometheus, OpenSearch, all together.
**Tobias Oka** 11:33 Nice.
Yeah, no, I mean, I… I will go through my notes again, because I… and every time when I was… when I was creating a PR, I was… I was writing some notes, but… about the stuff that I… that I realized, so… Nice.
Yeah, I think in terms of general improvements, I think there were some… There were some stuff… there were some things that… that felt like bugs, In the demo, but I haven't yet checked if they are already tracked somewhere, so I… that's just some cleanup that I will need to do when I wrap up my PRs.
To, to document that.
**Shenoy Pratik** 12:23 I have some things as, like, nits and pieces. I'm just discussing, like, what I'm thinking of improvement. It's around agents and agent observability. I myself have that in my backlog to get it done well.
**Tobias Oka** 12:34 That was actually also a thought, right?
**Shenoy Pratik** 12:39 So we have this agent flag and agent observability inside.
But the problem there was, it doesn't have few semantic entries that came in later, like session ID, which is… called GenAI Conversation ID.
So that part being added inside the LLM, request flows and all. It's not there today, in the agent demo.
So, I'm thinking of… Adding that as well.
Not sure if there are any other nits and pieces, that probably Datadog might have.
That we can update and make the Gen AI demo better.
**Tobias Oka** 13:20 I think what might also be interesting… is… The observability backend piece for that?
Because… Usually, for LLM observability, you, as an SRE, just look at this differently than, like, a traditional service, right?
Like, you can't just look at red metrics, like, you… You need to look at your evaluations and stuff.
So maybe there are some improvements.
**Shenoy Pratik** 13:56 eval is the other part that is pending. Yeah. Yeah. And what I've seen is eval is not standardized that way in Gen AI semantic conventions right now.
I need to talk to their SIG. But also, a custom eval dashboard, probably.
**Tobias Oka** 14:11 That's what I… that is what I… the end goal that I had in mind. Yeah.
**Shenoy Pratik** 14:16 Yeah.
I would say, if you have something, please, create an issue, at least, so we can start discussing there. I don't think, I don't want to push to… Rush into it, because we might need some more views from the actual… person who contributed the agent observability today inside the demo, Felix from IBM.
So, yeah, we can at least start an issue, and that will help. I can put in my views as well, and then… if we are good, then even I can contribute it in. But yeah, just creating an issue will be really helpful for the UAL side of things.
**Tobias Oka** 14:56 Okay, yeah, I'll note that down as one of the… so it might, it might take a bit of time until I… because I don't want to just write two sentences, I want to actually, like, think about it a bit, and word it properly, so it might… I might not do it immediately now, today, because I need to wrap up some other.
**Shenoy Pratik** 15:14 Yeah, yeah, it's fine. There's no expectations with our, SIG anyways, like, it's just whenever you get time.
If I, yeah, if I get time, even I can go ahead and create it, so that should be fine.
I'm just noting it down, that Agent EVR is something that we want to add to the demo.
Yep.
**Tobias Oka** 15:43 Maybe, and the dashboard.
**Shenoy Pratik** 15:45 And dashboard, yes.
**Tobias Oka** 15:46 for them.
**Shenoy Pratik** 15:51 Or the, Yeah, dashboard, I can… I think we can just work with Grafana right now, and if it gets… superseded by Percies, we can just update the dashboard there.
It's easier in Percy, is what I've heard, because their dashboard has code.
So it's a YAML configuration that you just uploaded, and it works.
Cool stuff.
**Tobias Oka** 16:12 Nice.
**Shenoy Pratik** 16:13 Nice, Yeah. Do you have anything else to discuss today? If not, then you should be fine.
**Tobias Oka** 16:21 No.
**Shenoy Pratik** 16:24 That's awesome, then.
Thanks, Tobias.
Later, yeah.
**Tobias Oka** 16:29 Bye-bye. See you. Cheers.
