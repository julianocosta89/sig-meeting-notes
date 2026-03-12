SIG: Community Demo App SIG
Date: 2025-12-17
Duration: 33 minutes
Zoom Recording URL: https://zoom.us/rec/share/xm4G36ZTKvCkwT6jhAbDU7C5axgWfFTKO_lnnWTbzKmWXU5vrD6kmPYE2nUCIqNh.e1Q6z_kI_FurcFhz
============================================================

## Zoom Recording Transcript

**Pierre Tessier** 02:15 Juliana, how's it going?
**Juliano Costa | Datadog** 02:27 Hello, hello!
I'm good. How about you?
**Pierre Tessier** 02:31 I am doing great.
I got to play the demo last night, this morning a little bit more.
**Juliano Costa | Datadog** 02:43 Awesome. I saw someone reacting to your, change of role, and I was like.
Huh, I'm not connected with Pierre yet. Why?
**Pierre Tessier** 02:52 I know, I realized that as well, and I was like, we should connect.
**Juliano Costa | Datadog** 02:58 We have been working just for… 3 or 4.
**Pierre Tessier** 03:02 Something like that.
**Juliano Costa | Datadog** 03:03 Yeah.
**Pierre Tessier** 03:04 I'm now gonna get a lot more time working on the demo, for what it's worth. I know I've told you this before, like, it's coming, it's coming. Well, it finally happened.
Last week we started the transition, and this week we kind of made it official.
So, and, the most best part was me just removing all these meeting invites on my calendar, just… mass deletes, leaving a whole bunch of Slack channels.
**Juliano Costa | Datadog** 03:28 Oh, boy.
**Pierre Tessier** 03:29 Give me the time to do things. So…
**Juliano Costa | Datadog** 03:31 This… this is, like, the… the… the meme, the cliche meme, like, ugh.
**Pierre Tessier** 03:37 Yeah, totally.
Very much.
Very much so.
So right away, I picked up, like, I got a couple things. I even submitted another PR, and I seen… it looks like it already got merged, to update some memory limits, because I had been running the demo for longer term on the side as well, getting it ready, and I noticed accounting's restarting all the time, and I finally figured out Prometheus. I got Prometheus to be stable.
**Juliano Costa | Datadog** 04:00 Awesome.
**Pierre Tessier** 04:02 Yeah. This is good, yes.
Yeah.
**Juliano Costa | Datadog** 04:06 Yeah, I have it running for, I think, a month on a local cluster here. Well, not a local cluster at EQS. Let me just get some… some stuff.
**Pierre Tessier** 04:17 How often… how often did the accounting service restart on you?
**Juliano Costa | Datadog** 04:20 Yeah, that's why…
**Pierre Tessier** 04:22 solid.
**Juliano Costa | Datadog** 04:22 But .
**Pierre Tessier** 04:23 Yeah, yeah.
**Juliano Costa | Datadog** 04:23 Share with you.
One sec, I need to authorize, allow, thanks and address.
Okay…
**Pierre Tessier** 04:35 Yeah, you probably have a similar AWS auth than we do.
**Juliano Costa | Datadog** 04:40 So, my nodes are 26 days old. That means I deployed the demo 26 days ago.
Accounting restarted.
1,240 times.
**Pierre Tessier** 04:58 Not bad! I've been running for 36 days now, and I've only got 76 restarts.
**Juliano Costa | Datadog** 05:04 Oh, okay.
Yeah. I have other concerning ones, like, Kafka 84 restarts, low gen 19, not bad.
**Pierre Tessier** 05:18 I don't have research on Kafka at all.
**Juliano Costa | Datadog** 05:20 Interesting. And also, I have Postgres restarting twice.
**Pierre Tessier** 05:25 Yeah, I…
**Juliano Costa | Datadog** 05:26 With Postgres, we have an issue that Severin brought up.
**Pierre Tessier** 05:32 Got an ugly one of both rest.
**Juliano Costa | Datadog** 05:34 Yes.
**Pierre Tessier** 05:35 If you run the demo for an extended period of time, you will eat up your temp space, and you will blow up. I have a solution for it.
Roll the deployment.
when you roll the deployment, it'll nuke its temp space, and it'll recreate its init directory. And I think we should probably include maybe a cron job, Pod that runs once a week.
that restarts a couple things, was my idea. I'm about to try that here internally.
So, there's some things in the demo. We already do it for our own demo today that we run at Honeycomb.
We do this more because we want the failures to always happen at the same time of day. So at midnight, we restart the key services in a demo, so it restarts all its own internal clocks, so the failures kind of happen on a pattern, it's like 4 hours and, like, 10 minutes, or something like that, our pattern, and it just works. So you know that 8am every day, your time.
The failures that, you know, that's what you get.
the hotel demo, because we do some things, like, Postgres just keeps on writing records.
Eventually, you're gonna run out of hard drugs.
**Juliano Costa | Datadog** 06:43 Yes.
Yeah, makes sense.
**Pierre Tessier** 06:47 Does it make sense to just restart postcards? You don't care about those records over time. And can we document it and saying, hey, look.
maybe even make it an option. When you run… when you sell this with Helm, we're… For long-term running, we're going to restart things, so things will reset every…
**Juliano Costa | Datadog** 07:07 Yeah, I… the only thing that I don't know how to do is… one thing that we discussed is that we want to drop the helm, right? Or, no, actually, not drop helm. We want to drop the Kubernetes manifests.
So we can implement that in help, then we are.
**Pierre Tessier** 07:25 Yeah, you would implement it in Helm.
**Juliano Costa | Datadog** 07:26 Yeah, yeah, yeah, yeah, yeah.
**Pierre Tessier** 07:28 It would deploy a cron job, which is based on… there's a kubelet image out there that exists?
or kubectl image that exists out there, you make sure it has a service account so it gets authorized properly, and you just have it run kubectudl, the deployment name, role.
And you're done. And it just restarts Postgres for you.
or restart, whatever it is. Like, however you restart a deployment, right? Yeah, yeah. Restarting the pod does not do it. You have to restart the deployment. That's the only catch.
Yeah, sweet.
**Juliano Costa | Datadog** 07:58 You can restart the deployment or delete the pod, but yeah.
**Pierre Tessier** 08:02 No, deleting the pod… I don't know if deleting the pod fixes it. It might.
But I would restart the deployment, because restart the deployment, make sure everything stays healthy. Because if something tries to write to Postgres, when you're leaving a pod, you might get a weird service hang-up somewhere else.
**Juliano Costa | Datadog** 08:16 So let's just do a restart, because the restart will at least allow it.
**Pierre Tessier** 08:20 To not go into an unhealthy state.
And… that was my big one on that one. I still have to do more tests for Prometheus, because I think Prometheus is maybe affected by it, but I think Prometheus is fine now.
Although I'm seeing mine, there was a weird thing that happened, and I don't know if I did that myself by accident.
Because it happened 2 days ago, and that was probably me when I was in here poking around and shit with Postgres.
**Juliano Costa | Datadog** 08:50 Let me just add the notes here, so we keep track of.
One thing that, so Roger pinged me because, we had an open chat, and he said that he wouldn't join today, but he wanted to share this.
So, I will, adhere.
to the dock.
Jesus.
Thank you, Google, for being so… So he's playing with this Rust Headless Chrome.
to replace… The logic that we currently have.
So, I don't know…
**Pierre Tessier** 09:44 There's a benefit here, just a memory thing.
**Juliano Costa | Datadog** 09:47 Yeah, well, yeah, I think so, because I think today Logen is the biggest service that we have, the…
**Pierre Tessier** 09:55 Yeah.
**Juliano Costa | Datadog** 09:55 It's huge. By consumption.
And, yeah, I wouldn't mind having a Rust example.
**Pierre Tessier** 10:05 Yeah, my low gen right now is consuming…
**Juliano Costa | Datadog** 10:08 Nope.
**Pierre Tessier** 10:08 I don't think this is right, but it says 6 gigs of memory?
**Juliano Costa | Datadog** 10:11 Only Logan.
**Pierre Tessier** 10:15 F.
**Juliano Costa | Datadog** 10:16 Oh,
**Pierre Tessier** 10:17 Hold on, this can't be right.
**Juliano Costa | Datadog** 10:19 Yeah, now I need to check mine.
Okay.
**Pierre Tessier** 10:33 No, this is not right, somebody's modified this, don't, don't… no.
**Juliano Costa | Datadog** 10:36 Okay.
**Pierre Tessier** 10:38 I take that ball back.
**Juliano Costa | Datadog** 10:40 I will, take a look at my… where is… Load generator, and I'll go to my service manager.
**Pierre Tessier** 11:03 I will…
**Juliano Costa | Datadog** 11:03 Yeah, so…
**Pierre Tessier** 11:05 Back to you on that one.
**Juliano Costa | Datadog** 11:06 Yeah, memory usage, on my end for the low gen is 1.5 gigas.
**Pierre Tessier** 11:14 It's big.
**Juliano Costa | Datadog** 11:15 No. Yeah.
**Pierre Tessier** 11:16 He consumes a lot.
And if you want to throw more users at it, it needs even way more memory. So, I am all for doing this if it actually saves us on memory.
Look, load gen also consumes more compute than anything else. I'm less concerned about that, because we're really… we're much heavier on memory than we are on compute.
So I'm all for anything that could Diminished memory footprint.
In every way possible.
Now the downside here is that we get… Locus gives us a nice UI for the low gen.
would we get the same thing out of this headless Chrome thing?
**Juliano Costa | Datadog** 11:57 I have never heard of this, so he shared the message, like, Half an hour angle, so I… I have no clue. That will… Do you use the… the UI from low cost?
**Pierre Tessier** 12:15 No, but it's there.
Every once in a while, I use it to stop the test.
So I could force traffic through, the web tier and make sure it's just my traffic.
**Juliano Costa | Datadog** 12:28 Because when tests are running, it's hard to see just my traffic.
Yeah, what I see, I… when I… when I need to do that, I kill the… the low gen.
**Pierre Tessier** 12:36 That's… that's a totally different way to do it, too. Yeah, yeah. But, like, in Kubernetes, it's… But you're right, you know.
**Juliano Costa | Datadog** 12:42 Yeah.
**Pierre Tessier** 12:43 it's easy for it to stop and restart the test. I'm gonna try some things, I'm just gonna deploy one single service and retry a thing.
That's why I used it.
**Juliano Costa | Datadog** 12:58 We haven't, I don't think we… we had a call together since the… Product reviews were, was merged.
But… I played with it, yeah.
I want to bring up something that I was… trying to investigate, and I… I failed miserably… miserably? Miserably?
And, So… Currently, in the demo, we have… if you go to the Docker Compose, and go to the… I think it's, like, 500-something. 500… 38.
We have this all-time instrumentation gen AI capture message content equals true.
So, in theory…
**Pierre Tessier** 14:01 Oh, wait.
I don't see what you're seeing.
**Juliano Costa | Datadog** 14:06 Let me share my screen, one sec.
**Pierre Tessier** 14:08 You said, which line is it? Oh, I'm sorry, 538, I was… okay.
**Juliano Costa | Datadog** 14:12 Yes, that's right.
**Pierre Tessier** 14:12 HubSpot.
Okay, hotel instrumentation gen AI capture message content equals true, yeah.
**Juliano Costa | Datadog** 14:18 So… In theory, that whenever the user asks, like, hey, is this product recommended for a kid?
This message, this text should be recorded as a SPAN event.
I think SpendEvent is the… the default.
Currently, we have, A custom attribute that has app.
add something like, ID, and add something Question?
that we are adding the question there. But this actually shouldn't be required. This Gen AI capture message should be captured automatically.
So, I asked the guys on the… the Gen AI hotel channel, and the guy said, hey, we have this new thing here, now we… with the new semantic conventions, this doesn't accept, a Boolean anymore, it accepts a known.
So I played around with all the possible ways, and it didn't work, so I opened Aisha to the Python, to the Python repo, but I wonder if that actually ever worked. So, now I don't remember. Because we have the PandaBot updating dependencies, so that maybe broke stuff?
With new releases.
But yeah.
**Pierre Tessier** 15:55 So, right now, if you turn it on or off, it doesn't do anything?
**Juliano Costa | Datadog** 15:59 No. So, like, true or false doesn't change anything, and also it's changing for the num, and using… there is another environment variable, of course, to use the newest symmetry conventions.
So if you use this new one, you need to change the boolean for the num.
And, yeah, I tried, like, text, I tried, uppercase, lowercase, whatever. All the combinations possible didn't work, so I just opened the issue and hoped for the best. But the Python REPL has, like.
400 or something issues open, and, you know, I don't know if I will ever get a reply, so…
**Pierre Tessier** 16:47 Yeah, I don't see any… Span events at all.
in product reviews.
**Juliano Costa | Datadog** 16:54 So… Product reviews, traces, there are two traces. One that has 10 spends, and one that has 11.
you should look for the traces that have 11 high spans. Those are the ones that are actually calling the LLM.
**Pierre Tessier** 17:15 Mine will have 3 or 9.
**Juliano Costa | Datadog** 17:21 Okay.
of…
**Pierre Tessier** 17:23 Are you sure these things are still arriving? No, no.
Or do you mean 11 spans in total? Or just 11 spans from the product review?
**Juliano Costa | Datadog** 17:35 I don't know, 11, 11 spends the whole trace.
**Pierre Tessier** 17:40 Oh, I…
**Juliano Costa | Datadog** 17:43 User as Product AI Assistant is the one, right?
I… Don't remember.
One sec.
**Pierre Tessier** 18:04 Can you summarize? Like, I see the question as a custom attribute here, can you summarize the product reviews?
**Juliano Costa | Datadog** 18:09 Yes, exactly. So this is a custom attribute, and it shouldn't be a custom attribute. It should be…
**Pierre Tessier** 18:16 It's fire control.
**Juliano Costa | Datadog** 18:17 Yo!
**Pierre Tessier** 18:19 the LLM call.
**Juliano Costa | Datadog** 18:20 Yep.
And it is.
**Pierre Tessier** 18:23 And…
**Juliano Costa | Datadog** 18:23 We have the environment variable there, so maybe Derek, when he, sent the PR, it was working, so that's why I wonder if… That actually ever worked.
**Pierre Tessier** 18:39 I could see it making… Get AI assistant response.
**Juliano Costa | Datadog** 18:51 Where his brother Cruz.
Oh, come on.
**Pierre Tessier** 19:05 Yeah, I don't see ANYTHING here.
Except for that one that we have, so maybe we broke instrumentation.
elsewhere.
**Juliano Costa | Datadog** 19:17 Yeah.
**Pierre Tessier** 19:20 Yeah, because I don't see that span event anywhere in here.
Let me check…
**Juliano Costa | Datadog** 19:32 I don't know if you have that ready, I mean, one thing… so, why I'm asking you this is that… I wanted to cut a release before, holidays.
**Pierre Tessier** 19:47 Yeah. So we actually have the product reviews usable for everyone.
**Juliano Costa | Datadog** 19:52 But if not… if it's not working, then I… I don't know if we should…
**Pierre Tessier** 19:57 Well, it works, it just probably, it still needs some cleaning up.
for… some… I think we still have some telemetry bugs in it.
But overall, it gets you what you want, just some of the attributes are wrong.
**Juliano Costa | Datadog** 20:17 Yo.
I mean, the attributes are not wrong, they're just… Not captured.
I, I, I…
**Pierre Tessier** 20:25 Yeah, this question should be part of the actual Gen AI call. So this span called chatastronomy-lm.
That should be where I would expect to see the question.
**Juliano Costa | Datadog** 20:37 Yes.
And we do, like, Gen AI response finish reasons.
**Pierre Tessier** 20:43 Yeah, like, I guess the input token's 58, so clearly…
**Juliano Costa | Datadog** 20:49 We are capturing stuff, yeah. And this is… if we check the scope name, the instrumentation is taking care of that, so this is not a, a metal span or anything. Different from the.
**Pierre Tessier** 21:04 Yeah, and then I can see output tokens is 43, so input was 58. And now the input tokens would include the description from the other products as well, right?
**Juliano Costa | Datadog** 21:17 The what?
**Pierre Tessier** 21:18 It would include the question, as well as the description from the other products, would be the input.
**Juliano Costa | Datadog** 21:24 Yo.
**Pierre Tessier** 21:26 So, maybe how we're presenting it today.
As the chat question, because it's… that's not the entire… the entire prompt is the question plus the other descriptions.
**Juliano Costa | Datadog** 21:39 Yes?
**Pierre Tessier** 21:42 That's… which forms the input tokens, because I was going to say, like, 58 input tokens is a lot for that really short question. Can you summarize the product reviews? Which makes sense, because it includes all the other descriptions.
**Juliano Costa | Datadog** 21:53 Yep.
**Pierre Tessier** 21:56 So, I don't know if the GenAI model knows the difference between what was the question and what was the context.
Because it just sees one big prompt.
**Juliano Costa | Datadog** 22:08 Mmm.
**Pierre Tessier** 22:10 So maybe what we're doing is good, but I would still rather have that question part of chat.
you know.
It's one span below. It's one span two, you know.
at that product in question, probably belongs more to, like, genai. whatever the… I think we have all the data today. I think there may be things we need to do, and Gen AI, Ali's still evolving, where we work with the SDKs to make sure that we have all the right things captured.
But yeah, some shit.
Yeah, we should cut this.
So, that's…
**Juliano Costa | Datadog** 22:53 Okay.
One question for you.
Do you think, so, I saw that you… added a bunch of commits to… to Martin's PR.
**Pierre Tessier** 23:15 Yeah, or commits, yeah, I need to talk to you real quick about that PR. I have one question for it, and it's… and then I need you to approve it, because I made so many changes to it.
I worked with Martin on it this morning.
**Juliano Costa | Datadog** 23:25 to finalize the last couple things, just to clarify a couple things with them. For what it's worth, the majority of the PRs were just linter errors.
**Pierre Tessier** 23:32 They kept on hitting this morning, like, oh my god, never frickin' said winters.
reason why it probably didn't work for some people was the ports he had hard-coded in a couple spots, and his NGINX… For the… you should not have a past rewrite on it, because of the way the thing was starting up.
I cleaned all that up, I made it so the port is now dynamic versus… based on an environment variable, NGINX routes the data properly. The only question I have is, do we want to use the endpoint telemetry or the endpoint telemetry dash docs?
That's the only question I really have.
**Juliano Costa | Datadog** 24:12 what is your opinion on that? I… I don't have… I don't think I have strong opinions.
**Pierre Tessier** 24:19 I think… so the service is already called Telemetry-Docs.
And I feel like it should be telemetry-docs, and it should be that.
Because maybe one day, we might want to open up a way for you to see a stream of telemetry at the telemetry endpoint.
I don't know if that would ever be a case, but, you know, maybe one day there's a way to to do a thing. I don't know.
But, so I think Kamachi Dogs feels better for me.
But, like, I don't care.
That was the only thing.
**Juliano Costa | Datadog** 24:55 Okay.
the only thing I discussed with Martin, on Slack.
was… Like, it was before he sent the PR. We were discussing about the PR, because he… He kind of teased everyone in the…
**Pierre Tessier** 25:13 Yeah. A little bit.
**Juliano Costa | Datadog** 25:14 Never opened a PR, and then I reached out to.
**Pierre Tessier** 25:16 Then finally he opens the PR, and by the way, he's been talking Weaver internally at Honeycomb for, like.
4 or 5 months now.
So… Yup.
**Juliano Costa | Datadog** 25:25 No, a waiver is great, and the only thing that I want to ask you is.
So, the way that he has here now.
Okay, let me try to start again.
I personally use Weaver to generate docs, generate code, so let's say that I have an attribute, then I want to generate…
**Pierre Tessier** 25:51 generate.
**Juliano Costa | Datadog** 25:52 Java… Yep.
**Pierre Tessier** 25:53 Yep.
**Juliano Costa | Datadog** 25:53 my Java class with all the attributes, perfect.
And, the live check to validate the telemetry.
So whenever someone opens up here, I have a load gen that sends, I have a request that goes through the service, and then the service emits OTLP to Weaver, and Weaver validates the telemetry that it receives.
**Pierre Tessier** 26:20 Yeah, yeah.
**Juliano Costa | Datadog** 26:20 Yeah, left check. This, those are the three things that I've been doing with Weaver. I know that there is the… another one that uses Rego for, I think, policy validation or something. I haven't checked this one yet, like, schema validation, whatever.
But I haven't reached that level.
So, my question is, finally.
Should we have a running service for Weaver?
Yes. We…
**Pierre Tessier** 26:54 you should probably, part of our CI, have a running service for Weaver.
That we spin up.
Only for CI reasons.
maybe make it optional? I get what you're saying for the… that's for live check, right? You'd run Weaver Live?
**Juliano Costa | Datadog** 27:10 Yeah, not just that, the fact that this telemetry, telemetry dash docs is, basically a documentation for the demo.
Should we have that as a service on the demo, or should we have something that, using Weaver, we update the docs on the OpenTelemptory.io?
Which is where our daughter.
**Pierre Tessier** 27:41 did the demos, Weaver Telemetry docs, be the same docs files that we have on… OpenTIO docs?
**Juliano Costa | Datadog** 27:49 So, all… all the… Not the way we have now, but the 70 Conventions docs are generated with Weaver.
So a win…
**Pierre Tessier** 28:01 When it was Weaver today.
**Juliano Costa | Datadog** 28:02 Oh, yes.
**Pierre Tessier** 28:04 On, on, on… so we would just add that, but for… So what we do… so we would use Weaver to generate the same docs.
Or the schemas that we maintain in the demo.
**Juliano Costa | Datadog** 28:15 Yes.
**Pierre Tessier** 28:16 And we might have to duplicate those schemas inside of the… the hotel.io repo, but that's fine.
Yes, we should. We should.
And we should have, like, a section in the demo. I think that makes a lot of sense.
And then, effectively, now, this telemetry dock service is just kind of a duplicate of the… Telemetry docs section inside OTel I.O. docs demo.
Or would we even still… So basically, this service that we have right now.
**Juliano Costa | Datadog** 28:53 Oh, that's good.
**Pierre Tessier** 28:53 telemetry Dock Service.
**Juliano Costa | Datadog** 28:55 Yes.
**Pierre Tessier** 28:56 It uses the schemas.
So we would replicate these schemas inside of the community… inside the OTel I.O. repo.
And we would run a… generate the Weaver markdown, whatever it's called.
The docs markdown, based on those, similar to how we do it today in the demo itself.
Or would we even care to still keep these things inside the demo? Would we just make these part of hotel.io?
**Juliano Costa | Datadog** 29:29 Yeah, that's my question to you, and maybe… I think Marty has a different opinion than mine.
And I, this is where we… we have… we had a…
**Pierre Tessier** 29:41 No, yeah, yeah.
Because our official docs is really OpenTelemetry I.O. docs.
**Juliano Costa | Datadog** 29:47 Yeah, and I, like, when you are running the demo, why do you want a service with the docs? This is where I didn't get from.
**Pierre Tessier** 29:56 So you can see the telemetry that's available for you.
But… Really, you should be just going to docs.opentometry.io forward slash demo… Elementary, whatever the hell. Yeah, yes, So, should all of this, what we just did, be better served to be part of… OTelio.
And if anything, we just provide… Documentation, or like, hey, go see the telemetry available here.
**Juliano Costa | Datadog** 30:28 I don't know, because… So, like… The value of having the… all the… All the attributes defined here is that we can later run the live check.
**Pierre Tessier** 30:44 It's locally.
**Juliano Costa | Datadog** 30:46 If we… well, unless… no, actually, if the schema is on the demo, is on the…
**Pierre Tessier** 30:53 And we'd be…
**Juliano Costa | Datadog** 30:54 It is on the OpenTele Entry I.O, we can query from there and use the schema from OpenTele Entry I.O. Well, good question. Now I'm, like, yeah, I don't know. So… Okay.
What… Yeah, I don't want to get into it.
**Pierre Tessier** 31:13 release if we're not gonna move it forward. That's right.
**Juliano Costa | Datadog** 31:16 Yum.
**Pierre Tessier** 31:19 Ugh.
This is the real problem.
That'll have your answer.
**Juliano Costa | Datadog** 31:28 Yeah, I also don't have an answer for that, and this is where I quite didn't get what Marty was telling me, and then now seeing it, like, I still… Don't know… how that would work, or why would that work? I think I have my… My discussion with him, no.
Man, I have another meeting now, so I will.
**Pierre Tessier** 31:56 Yeah.
**Juliano Costa | Datadog** 31:56 Absolutely.
**Pierre Tessier** 31:57 I know what you're saying, Let's hold off merging this for this release, then. Let's cut this release without it.
let's hold it for the next version, but I… I… I do think we should generate schemas in here.
Because the schema generation should be part of the actual source code.
And then we probably just end up copying those schemas back into OTELIO.
We already do that for a couple other files.
like, dashboard definitions and stuff like that with Helm, where we copy them over to the Helm repo. So, I have a feeling that's gonna be the process.
Schemas live inside the demo.
They get copied into the I.O. repo, And… we use… we render documentation inside the I.O. repo. We don't actually render documentation here. The only thing we use here is schemas is for live check.
**Juliano Costa | Datadog** 32:54 Yeah, we could keep the schema here, and without duplicating to the OpenTelemTree I.O, I think we can use Weaver in OpenTelemetry I.O. to generate, based on the schema.
**Pierre Tessier** 33:05 based on schemas and demo? Even better. Even better. But I think that's what we should be doing. That should be the angle we should be doing, and all this documentation should actually live inside of hotel.io.
**Juliano Costa | Datadog** 33:16 Awesome. Okay.
**Pierre Tessier** 33:18 Okay.
**Juliano Costa | Datadog** 33:18 cope.
**Pierre Tessier** 33:18 Cool. Go do your meetings. Appreciate it, man.
**Juliano Costa | Datadog** 33:21 See ya.
**Pierre Tessier** 33:21 Thank you.
