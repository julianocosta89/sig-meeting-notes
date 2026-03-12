SIG: Community Demo App SIG
Date: 2025-08-27
Duration: 24 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 01:35 Hello there.
**Jonathan Munz** 01:37 How's it going?
**Juliano Costa | Datadog** 01:39 All good. Yourself?
**Jonathan Munz** 01:41 Good.
It's on, … PTO for a few weeks, so just getting back into….
**Juliano Costa | Datadog** 01:49 Yeah, same. I just… just got back this week, so….
**Jonathan Munz** 01:53 Oh, nice.
**Juliano Costa | Datadog** 01:54 Still, still catching up all GitHub notifications.
**Jonathan Munz** 01:59 Good luck.
**Juliano Costa | Datadog** 02:01 Hey, Matthew. Welcome.
**Matthew Hensley** 02:03 Hello?
**Juliano Costa | Datadog** 02:06 First time joining this sick?
**Matthew Hensley** 02:09 It's… Maybe?
But if it isn't, it's been a while.
**Juliano Costa | Datadog** 02:19 Glad to have you here.
Before we start… Shannon, let me ask you one thing. Do you have folks from AWS working on OpenTelemetry, other than the Open search team?
**Shenoy Pratik (AWS OpenSearch)** 02:44 We have a set of people who are working on ADOT and contributing to, OpenTelemetry Collector.
I need to look… they're in a different org.
The Prometheus or something.
But, we had a good… group of people earlier who were contributing AWS receivers, logs, CloudWatch stuff to Collector.
I can get… get in touch with them.
**Juliano Costa | Datadog** 03:13 Is there any specific ask?
That's exactly what I wanted to know, because if you checked the… Let me paste it here. If you check the releases… for the OpenTelemetry collector, on the… the release note.
**Shenoy Pratik (AWS OpenSearch)** 03:35 Or… contrib.
**Juliano Costa | Datadog** 03:38 I'm sure he's here.
**Shenoy Pratik (AWS OpenSearch)** 03:42 No, I see. AWS CloudWatch Log Exporter, it's become unmaintained now.
**Juliano Costa | Datadog** 03:47 Yeah, we haven't passed.
a bunch of AWS stuff being, tagged as unmaintained, and eventually they will be Removed from the contrib.
this true?
Because there is no one… So there is no code owners for those components.
**Shenoy Pratik (AWS OpenSearch)** 04:13 Let me reach out to internal folks. I think we can get someone.
onboard again.
**Juliano Costa | Datadog** 04:21 Awesome.
**Shenoy Pratik (AWS OpenSearch)** 04:21 Thanks for pointing it out. I didn't know that.
**Juliano Costa | Datadog** 04:25 Cool, thank you.
Okay, on the… making notes… I think we have… Of course, I opened up.
Beautiful.
I just added a couple of, stuff here. Well, actually, two things. One is the new release that we are… … We should have one Zoom, or… I think we already passed that.
And, … A user opened an issue with, IPv6 compatibility.
And it's super well detailed, the ticket.
… I don't know if… but it's, like, easy to solve in order to kind of make it work to IPvC6 and IPv4.
But this looks like a good, thing to actually tackle.
What do you guys think?
Then I paste here on the chat as well, if we're not following on the docs.
**Shenoy Pratik (AWS OpenSearch)** 06:11 I think we should have support for both IPv4 and V6, that's for sure.
But I need to look into detail for this one, to understand, like, what are the changes exactly.
**Juliano Costa | Datadog** 06:26 So, the user mentioned that we need to kind of replace the 0.0.0.0 with column column.
I don't know if it's that simple.
And if it will work on, both ways?
kind of… we change, and then it starts working with IPv6, but then crashes all IPv4, so yeah, this is what we need to kind of test and see.
But, yeah, I'm happy that he actually… the ticket is well structured, so… My truth.
he wrote down everything, or if it was AI.
But… Either way, it's… it's cute.
**Shenoy Pratik (AWS OpenSearch)** 07:18 Good point to start with, at least, yeah.
I think it should be easy enough, like you mentioned, but only thing is, does Docker or Envoy go into any issues or not?
The only product I'm thinking of right now.
**Matthew Hensley** 07:41 I'm… fairly sure, one of my colleagues here at Grafana has also ran into this when they were Provisioning the demo.
Kubernetes and… happened to only have IPv6 networking enabled, to do some other testing, and obviously, it didn't work, so….
**Juliano Costa | Datadog** 08:02 Do you know if your colleague fixed it?
Somehow….
**Matthew Hensley** 08:06 They did not.
**Juliano Costa | Datadog** 08:07 Okay. Okay.
Because that happens a lot, Matthew, more than we… We wished people fixed their issues and never contribute.
Bye.
So, yeah, it's always good to ask.
**Matthew Hensley** 08:31 No, we would have upstreamed anything. We, … Make fairly common contributions to the demo when we find things.
**Juliano Costa | Datadog** 08:47 And, I just pasted the… 2448, the PR that… Should I open?
I have one question here. I saw that you are adding an extra container here, the open search init.
… Can you tell me a little bit more about that?
**Shenoy Pratik (AWS OpenSearch)** 09:18 I think the extra container might not be needed, because we are just using the official one and then removing a bunch of stuff from it.
**Juliano Costa | Datadog** 09:27 Oh, okay.
**Shenoy Pratik (AWS OpenSearch)** 09:28 We don't want to… we don't have to publish a separate image, like we discussed earlier, for another distribution.
So, that was, like, one of the ideas, too. We need to publish it in our, … Doctor space or not.
But I'll remove that. We'll just use the Docker file, get the… Main distribution, and then remove a bunch of stuff.
I thought the other way as well, but for our min distribution, we don't release Docker. We don't publish Docker images.
Where it's just a bare minimum open search, and then you can add plugins like PPL, SQL. That was the other route, but there I don't have the Docker image, so I'll have to create one.
So either I thought this one would be easier to maintain long-term, because you already get the official release.
**Juliano Costa | Datadog** 10:14 I see.
**Shenoy Pratik (AWS OpenSearch)** 10:17 But I'm yet to do some testing with LoadGen, and that's why I haven't… like, made it out of draft yet, to see if it actually makes stuff, or breaks stuff with Locust, if I just ramp up something. Is there some limit that we test on with Locust? Because I know it will fail if you… plus some X number of users on the load gen.
So, do we have a number where you want to test OpenSearch with X number of users?
And locust, and still make it work.
**Juliano Costa | Datadog** 10:48 … I don't have any… Pardon?
a code for… a hard number for that, but, I know that we have, A feature flag to increase the number of, load.
Let me get that.
So, it's called, Load Generator Flute Homepage.
That just increased the amount of requests and….
**Shenoy Pratik (AWS OpenSearch)** 11:27 Makes sense.
then I'll try to see if that doesn't break logging, otherwise we won't be able to ingest it.
It shouldn't be that. Opens as it still starts failing with the flood, yeah.
Cool, I think… yeah, that would be a good benchmark then, yeah.
**Juliano Costa | Datadog** 11:46 Nice.
… Yeah, anything else? Anything that… Anyone want to discuss?
**Matthew Hensley** 12:11 I was, … Just curious… So, release-wise, it's obviously been a few months. Is there… I guess… is there something about the process that's… Making it… Take that long?
Or….
**Juliano Costa | Datadog** 12:26 Not really. So, yes and no.
… So… we just need to take time to release. So making the release on our own repo is easy.
The problem is that we touched a bunch of stuff, that affects the Helm charts.
And, currently, Pierre is kind of the… the main person touching how?
And it's been busy for some time, so… I need to put some time and… do it. It's not, like, … it's not difficult, it's just you need to go through all the changes, ensure that all environment variables that we updated on the demo are also reflected on the Helm chart, so this is a bit, … Minimal, so….
**Matthew Hensley** 13:25 No doubt, I… obviously, it's… A huge codebase, and it's all… Yeah.
all a little bit different, it's not simple at all, so… I was just curious if there was anything, in particular besides just… Needing time because of how big it is.
**Juliano Costa | Datadog** 13:41 Yeah, no, it's just that, yeah, I just need… I said I would do before going on holidays, and I haven't, so that was 2 weeks ago, so… I'll try to… To put some time in to do that, this week, or… Next week, so….
**Matthew Hensley** 14:02 Okay, thanks.
**Juliano Costa | Datadog** 14:03 I said, I understand the….
**Matthew Hensley** 14:04 one, yeah.
So, yeah.
**Juliano Costa | Datadog** 14:13 Boom… Well, if we don't have any… anything else, I just want to… to raise one thing… one question to… to Jonathan.
Jonathan, do you have any… Do you happen to have any, any time to maybe consider Getting the… the mobile app, … Like, doing the changes that we… we did.
We kind of… Well… It discussed at the beginning, so to say.
The one that I'm more interested in is in… trying to… I don't remember the proper framing, but, like, trying to make the app on my mobile… on my phone to connect to… somewhere else, so I just point the app to, to the… Point that to a demo running.
Jesus.
Yeah, I think we… we discussed about that before, right? Because at the moment, in the current setup, everything has to be running locally on the local host.
So, it would be awesome if we start a demo somewhere, let's say AWS, and then open the app, and in the app, we just add the address for the demo, and then, like, the URL, or whatever, and then it works.
**Jonathan Munz** 15:40 Yeah, I think I'd have some time. I think, yeah, I had a few of these in mind from last time we talked about it. I think what would probably help… I believe we've filed an issue… But yeah, if we could dig up… I guess the wish list, and… and… figure out what is the top of that wish list, I'd probably have time to tackle, … the most, sort of, desirable behavior, if it's that one, or… I think there was a couple others.
Probably… Talked about, but yeah, that would be the most… Useful for me if there was, … if we could resurface that issue in the repo, and then I think it listed, like, a bunch of different things, and split out the one we think is the most valuable, and then I can… Find some time to… To tackle that.
**Juliano Costa | Datadog** 16:33 Awesome, yeah, I'll do that.
Just paste… pasting on the… on the doc.
They should… There are a bunch of stuff here.
**Jonathan Munz** 17:44 Right, so, and the one you just mentioned, that was the first checkbox.
**Juliano Costa | Datadog** 17:46 The first one, yeah.
**Jonathan Munz** 17:48 UI to configure. Okay. Just taking a look if there's anything… Else that we should consider?
**Juliano Costa | Datadog** 17:54 To be honest, I don't know how easy it is to do that, because, I mean, configuring the UI to access the demo, I think this is… fairly easy, so to say. The problem is how you're gonna configure, or at least We need to think about how we're gonna configure the… The mobile app to send data to the collector.
So, how that will work? So, this is the tricky part.
**Jonathan Munz** 18:24 Yeah, so is there, … I've only ever run the demo, locally. Is there sort of a… Documentation or a way to set it up.
That it's running on a publicly access… including the collector, like, a publicly accessible… … Infrastructure.
**Juliano Costa | Datadog** 18:49 That's a good question. I don't think our, … our docs… The only thing that we say here on the Kubernetes deployment is… That you can… Where is it?
That you can configure, for instance, a load balancer.
**Jonathan Munz** 19:13 But we just….
**Juliano Costa | Datadog** 19:15 We just mentioned that for the front-end proxy, which is the entry point for the whole web.
**Jonathan Munz** 19:23 Which makes sense.
**Juliano Costa | Datadog** 19:24 But… We would also need the collector, right, to be exposed.
But is it….
**Jonathan Munz** 19:31 The, … so wait, so currently you can run the, like, the front-end So… I guess the analogy would be, can you run the astronomy store website.
Somewhere that someone could just hit publicly in a browser, and then that telemetry is sent off.
Does that work?
Currently.
**Juliano Costa | Datadog** 19:51 Yes, but what happens is that… you run everything, let's say, in a EKS, in a cluster.
**Jonathan Munz** 20:02 And you expose the front end.
**Juliano Costa | Datadog** 20:06 Or… or the envoy.
And that's it. So, people re… so the user will… reach the invo endpoint, and then the whole application will load, because all the services are running with… inside the cluster, inside the same cluster, and they can talk with each other, and all the telemetry Flows through to the… through the collector, and the collector sends the data somewhere.
the point that I'm saying is that We do not have anywhere else the collector exposed as well.
**Jonathan Munz** 20:40 Right. So does the… but, like, the browser code is instrumented with the… the, like, JS SDKs, right? So, like, in the example, in the setup you just described, if I'm on some other computer in some other part of the world.
and I load that website.
The telemetry from my browser… Is somehow able to be sent.
**Juliano Costa | Datadog** 21:06 Yeah, and … There is a section here, configure browser telemetry. There is a public hotel exporter, OTLP traces and point environment variable.
**Jonathan Munz** 21:18 Okay. And for this one, we set the….
**Juliano Costa | Datadog** 21:22 The public endpoint for the… for the collector.
**Jonathan Munz** 21:25 Okay, so that would… I mean, that would be similar then. So, yeah. So, yeah, that would be… so that's a good… yeah, I think that's a clearer definition of the task, like… If, … basically wanting the same functionality we have for the browser side of the front-end proxy in the mobile app. So, yeah, if you have those links handy, then I guess the first step would be… for me would be to… Just to understand how it all works together, have that same setup, where everything can be running… somewhere, and then separately I can load up a browser, and then all that telemetry makes it where I'd expect, and then… Be able to make it possible to do the same thing With the mobile app, as you would in the browser, because that's the… that's the analogy, is the browser and the mobile app, so as long as that flow is works how we'd want it, then I would use that as a model for… perhaps want the mobile app. Yeah, that sounds good to me. And yeah, looking at the other list, I think that feels like a good… one to tackle, I mean, the rest is adding in, like, other pieces of the demo app. … I know we tar- talked about… like, releasing as an APK and things like that, but this feels almost like a prerequisite, because you would want this flexibility To have it be… worthwhile to have, like, a package version of the app and everything, so….
Cool, yeah, I can, make a note of that and, and try and find some time and update next.
Next, meeting.
**Juliano Costa | Datadog** 22:59 Awesome.
Yeah, no, no pressure on that, actually. I just wanted to bring that up again.
**Jonathan Munz** 23:06 No, it's good, I know, because we… this was… this was many months ago now, and it's good to… it's good to… have some… Update, just to keep it going, and … and this feels like a good… Next step, that wasn't, … done in the first iteration. So, yeah, I like that as a task.
**Juliano Costa | Datadog** 23:28 Awesome.
Thank you.
Boom.
Okay.
Then, if… That's it. Then… See you all in 2 weeks!
Thanks for joining. Bye.
