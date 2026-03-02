SIG: Community Demo App SIG
Date: 2025-07-30
Duration: 37 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 03:04 Hello! There!
**Shenoy Pratik (AWS OpenSearch)** 03:08 Giuliano.
**Juliano Costa | Datadog** 03:10 How are you doing.
**Shenoy Pratik (AWS OpenSearch)** 03:13 Good. How about you?
**Juliano Costa | Datadog** 03:16 Good as well.
Yeah, busy. But yeah, good.
Ugh!
So
I I don't think we have. I I well, I don't think many will actually join so, and checking the agenda, there is
nothing here. So what I will just want to. What I just want to to discuss with you is
checking your comment on the
I think it was in on a on a thread, where we were discussing the size of
open search, and you said that the Java, the Java memory, was set to 300,
and you were expecting that 300 would fit. I did some testing, and 300 the the container not even starts.
It does work with 600.
So I'm not sure like. From what I from what I what I saw. I think we have something like that for. Go as well. Let me just open here and I can. I can tell you what I
what I mean, Bargo, we have.
Yeah, for instance, for a product catalog, we have a go memory goal memory limit of 16, and it
16 mebits, and
the the resource limit for the container is 20. So like there is a difference like a small difference. We do not set the limit to exactly the same memory limit. I think there is some.
I don't know why
but for for Java what I felt was that we needed something as well, so I I just like
reduced from one giga, which is a lot, but not but I saw that 300 also doesn't work.
hey, Pierre?
**Pierre Tessier** 05:38 Though.
**Juliano Costa | Datadog** 05:41 Hello! Hello!
**Shenoy Pratik (AWS OpenSearch)** 05:44 Did you see it go out of memory in 1.1 itself?
I think that was the main question. Right.
**Juliano Costa | Datadog** 05:54 The.
**Shenoy Pratik (AWS OpenSearch)** 05:54 Run it as a small footprint as possible. I think the contributor was seeing out of memory, not able to start on his machine.
**Juliano Costa | Datadog** 06:05 Yeah, I think he had a like a remote machine or something like that. And he was looking for a smaller version of the Demo, but he was still complaining about the minimal.
**Shenoy Pratik (AWS OpenSearch)** 06:18 I see.
**Juliano Costa | Datadog** 06:19 But because the open search need well open. Search also runs on the on the minimal. The only thing, the only 3 services that do not run on the minimal, are accounting fraud, detection, and Kafka, so everything else runs.
I he's he thinks I I still need to come back to him. He thinks the the Pr that I have drafted is to solve that. But it's actually not
so ideally. We would have some. I don't know environment variables, something to configure on the demo where, for instance, instead of calling, quote service. Don't call and then do not start quote service. So it's 1 less service to run. And we we could like configure the demo to run with a minimal set of
services. But this is a total different discussion. I I feel that the the change on open search will help us out on that, but they are not totally related.
**Shenoy Pratik (AWS OpenSearch)** 07:23 Okay, got it? Yeah. Then I'll I'll do. The thing that I mentioned can help so there are 2 ways. One is to get the open such minimal docker, which only contains the core, and add the SQL. And Ppl. Plugin for the queries that Grafana dashboards uses. That's 1 way.
The other way is to take the exact fully
full plugin compatible thing shipped that is there right now and then remove. Strip off the plugins that we don't use.
That's the other.
**Juliano Costa | Datadog** 07:59 Wow!
**Shenoy Pratik (AWS OpenSearch)** 08:01 I think stripping off the plugin is easier, because I don't know if min distribution is supported across all platforms. I need to check that.
So we can. We can take the production docker and then remove plugins that are not needed. So I can edit the docker file for it similar to how we do other
awesome.
**Juliano Costa | Datadog** 08:21 Cool. Yeah, yeah, no. If it's a multi-stage docker file, I think that would solve. And then we can limit the size of it on docker compose level.
**Shenoy Pratik (AWS OpenSearch)** 08:31 Yeah.
**Juliano Costa | Datadog** 08:32 I think that's that's nice.
Okay, okay. So I'll add that to you. Here on the notes.
Pierre, as you are here, we have a Pr.
Regarding Jaeger. 2 Jaeger version 2,
and on the docker side, on the docker compose file side. Everything is working.
But he is worried about the helm changes because there is no operator for Jaeger version 2 yet.
So I I tagged you there. I don't know how we're gonna handle that. I know.
**Pierre Tessier** 09:17 Write a Pr. To the Jaeger helm chart. I seem to be the only one who's maintaining that thing as well now, which is kind of silly.
**Juliano Costa | Datadog** 09:23 Oh! Who really?
**Pierre Tessier** 09:24 I don't update that helm chart very often in the Jaeger project with the latest version of Jaeger. So I've I've done several Prs to update the version of Jaeger on that on the helm chart
at this point. It's
I should probably join their Sig meetings. We should.
I'm starting to wonder if we should continue to sub chart Jaeger.
**Juliano Costa | Datadog** 09:55 Honestly speaking, if I don't see a reason for that.
Yeah, one container, right? Do we need to use the.
**Pierre Tessier** 10:07 No, I think we just figure out what that home chart spits out.
and then just do it ourselves as a separate either a component or
because because right now all the observability tooling is done through a sub chart for what it's worth. All Ollie tooling is done through that and all the demo sources are done through a component. So this would be different.
Is it still a component?
Probably not because I'm sure that that chart has a bunch of weird things to it.
which means we'd probably just have to have additional files specifically to roll out the the Jaeger components
as part of our deployment, and then we just reference those in a Jaeger section in the helm chart.
This would be a breaking change for sure.
so we'd have to provide upgrade notes on it as long as we. We make the upgrade. Not hard for people like. I don't think anybody's modifying Jaeger. Necessarily, when they deploy the the demo.
The only real things they would see people doing is is increasing the capacity of Jaeger.
right? So it allows to have more traces, for for reasons whatever give it more memory, give it more traces.
But yeah, this is, this has hit us multiple times. Now.
Giuliano like like even early days of Demo. It's, it seems, the helm charts always several versions behind on Jaeger.
**Juliano Costa | Datadog** 11:39 Yeah. The good thing is that not much has changed to be fair.
**Pierre Tessier** 11:45 Yeah, nothing. Nothing is changing anymore. And I and I feel like the development on Jaeger is pretty static at this point. All their changes are more around, plugging them deeper into the hotel ecosystem.
which don't seem to change other aspects.
**Juliano Costa | Datadog** 12:00 The thing that I noticed is that on Version 2, they are now shipping a collector which is weird, because now we're gonna have 2 collectors running.
**Pierre Tessier** 12:10 If the I have to go look at that
is the all in one already had the the
but the one we use is the all in one Jaeger, which includes all they do is they just use the collector to feed the data into Jaeger, that's all it is. But it's just like A. It's like a receiver that sits on top of Jaeger to feed the data. And so it's part of their all in one container is what they call them
if that's been changed, I would have to under understand a little bit more about how that's been changed. But
**Juliano Costa | Datadog** 12:39 Yeah. One thing that I well, I noticed that by looking at the the pr, so the Pr is 2389.
It's on indirect.
One thing that I that I noticed was that he created a a file called Eager Config, or the file is called config, and it has, like the same structure as
collector, and now it has a receiver and a exporter that exports to Jaeger storage, exporter.
**Pierre Tessier** 13:11 Which which Pr. Number was this.
**Juliano Costa | Datadog** 13:13 Based on on the are you on the on the docs, on the meeting notes.
**Pierre Tessier** 13:21 I can't be. Yeah, yeah. I was looking at the Jaegers repo, but
r or PR, yeah, yeah.
okay, yeah. That's the one I was.
I mean, do we need Jaeger? V. 2.
Can you come.
**Juliano Costa | Datadog** 13:48 I mean.
**Pierre Tessier** 13:48 In Kubernetes doesn't matter.
**Juliano Costa | Datadog** 13:50 So that that's the thing like
We don't need pgrv. 2, but
I'm running the latest Jaeger v. 1 in one of my my demos, and they started putting a notice, saying that they they gonna be discontinue. It.
**Pierre Tessier** 14:11 No, that's not a good note. Okay, let me.
**Juliano Costa | Datadog** 14:15 No, we we if if we're getting warnings, people are. Gonna say, stuff, you're right.
**Pierre Tessier** 14:20 So let me investigate a few more things here real quick.
So we're using 3, 4. 0, today, on that.
And the operators even further behind. It's like Jaeger doesn't care about kubernetes.
**Juliano Costa | Datadog** 15:04 I'm I'm not too familiar with
people not using proprietary tool because of my background. I it was.
**Pierre Tessier** 15:15 Yeah. Well, why would you? I don't use Jaeger either.
**Juliano Costa | Datadog** 15:18 Yeah. But like, do people deploy Jaeger and Grafana? Or do they deploy Grafana? And like
Jaeger is embedded somehow or no, they yeah, I I honestly don't know like.
because those are a lot of stuff to to manage. Why would you do that?
I mean, yeah, I understand why. But yeah.
anyways.
**Pierre Tessier** 16:00 And we don't do that one. We do the all in one.
all in one. There it is.
I'll need to investigate further.
How about this?
and.
**Juliano Costa | Datadog** 16:25 Okay, any.
any anything that you would like to discuss on your end? I have another thing that I would like to to
shed some light on, but.
**Shenoy Pratik (AWS OpenSearch)** 16:36 I have a question for eager. Why do these all in one? Why not?
Let's use whatever is needed, or do we use all these.
**Pierre Tessier** 16:45 One is much smaller. All in one is much smaller than everything else. That's why it's about the size of the demo here, right? We don't need this to be Enterprise stack quality. It needs to just run on somebody's laptop. So if you say, Hey, I want to back Edgar with elastic search. Oh, my goodness, it's good! It's way bigger way, faster.
**Shenoy Pratik (AWS OpenSearch)** 17:03 Using the all and using the memory store, keeps it much more compact.
**Pierre Tessier** 17:09 You know, we don't need to retain traces for more than a couple minutes. Even. We just need to showcase that it works if you if you have 30 min of traces, I think you're fine.
**Juliano Costa | Datadog** 17:19 Amazing.
**Pierre Tessier** 17:21 And I even recommend to use. If there's a way we can figure open search to drop logs after maybe 4 h, and if it saves us memory. That's not a bad thing to do.
right.
**Shenoy Pratik (AWS OpenSearch)** 17:32 Yeah, that is a way I can.
**Pierre Tessier** 17:33 Is also really big. And and you know, I I know, like, because when we think of enterprise configurations, that's 1 thing you want to be redundant. You want a storage. You want all these great things, but we're trying to build a demo, and and we should.
**Juliano Costa | Datadog** 17:47 I'm confused.
**Pierre Tessier** 17:47 Use a demo with production.
**Juliano Costa | Datadog** 17:50 Yeah.
**Pierre Tessier** 17:51 So if you know ways to configure open search, that it just sheds its logs, and if we're, you know, it drops logs after, I think probably 4 or 6 h, or something like that.
That would be fine, I think, if we just make a note about that. And hey, your logs are going to be dropped because of memory constraints. If you want to keep, change the setting in your appointment, and then you'll keep logs for longer.
**Juliano Costa | Datadog** 18:11 I think.
**Pierre Tessier** 18:11 That would be fine for us to document and to give to people. Because, like, like Juliana was saying, we have somebody's trying to deploy the minimal configuration. They can't, because they don't have enough resources.
**Shenoy Pratik (AWS OpenSearch)** 18:21 No.
**Pierre Tessier** 18:22 You know. So that's why we use Jaeger all in one.
**Juliano Costa | Datadog** 18:27 Another thing that that we discussed here was the playwright.
like we we couldn't find any other low gen that could generate like synthetic clicking.
**Pierre Tessier** 18:44 Yeah.
**Juliano Costa | Datadog** 18:45 But yeah, if if anyone knows anything, just let us know.
I did some testing. But I I couldn't find anything like open source and easy to use. Selenium is huge.
would be even more common.
**Pierre Tessier** 19:00 Internally at honeycomb. We use playwright through node instead of through python.
and it has significant savings in terms of memory consumption.
You know our load generators written in Python? Could we just rewrite the load generator and and node, or use a node based load generator that leverages playwright through that. Would that save us something? I don't know. But I know at Honeycomb, when we do this kind of stuff we just run playwright, straight up as a node container, and we're done.
**Juliano Costa | Datadog** 19:25 Okay, yeah, that this is good to know.
So as as we are talking on that about that one thing that I also so I'm working on a Pr that changes the
all the compose, all the docker, compose files into one, compose file with profiles
that would change the way that people are deploying the demo. So like, of course, if they use make, I will just update the make comment. But if they do, Docker compose the the difference would be that they need to do like docker, compose, dash, dash, profile, full, or minimal up, and if if they need to build as well dash, dash profile, full build minimal build minimal up full up.
And that's the only difference. Again, if they're they're using make, I'm gonna update that on make. But this reduces a lot.
**Pierre Tessier** 20:29 Default, profile.
**Juliano Costa | Datadog** 20:32 We can when they complete.
**Pierre Tessier** 20:35 Default, profile be everything, and then minimal removes things. Or is that not the way it works?
**Juliano Costa | Datadog** 20:39 It's so.
So that's the thing I was thinking about using the the the fullest Jesus as the fall.
But there is no way, using profile to unset environment variable.
So what what happens is that I set the Kafka and the Kafka address all right.
Checkout service to empty as default.
and when I run the full
I add the Kafka to that container
I add the Kafka addr to that container, because
if I do the other way around on minimal. I cannot unset my environment. Variable.
I I try to.
**Pierre Tessier** 21:36 Can we just create an environment variable called use? Kafka equals true or false. And then we just flip it, based on which mode and have checkout. Use that instead
to determine if it's going to talk to Kafka, because right now we just check to see if the environment variable is empty
or not. And if it's not empty, we use Kafka. Can we just make it be based on something else instead.
**Juliano Costa | Datadog** 21:56 Like a chew of.
**Pierre Tessier** 21:57 You know what I mean, like a yes or no type of deal.
**Juliano Costa | Datadog** 22:00 Yeah, that I think that that's easier.
**Pierre Tessier** 22:03 You could change one. You just can't unset it right.
**Juliano Costa | Datadog** 22:06 That's.
**Pierre Tessier** 22:06 The struggle.
because the way we're looking at it, we're looking to be set or unset in code. Why don't we just say be set to.
you know. Now, it needs 2 environment variables like, I don't think that'd be difficult to do and
checkout. We just modify the code to say, you know.
Do you use Kafka? Yes or no?
**Juliano Costa | Datadog** 22:27 Yeah, that that would do.
**Pierre Tessier** 22:30 Okay.
**Juliano Costa | Datadog** 22:32 Question on that.
**Pierre Tessier** 22:33 If we could have a deep.
**Juliano Costa | Datadog** 22:34 Funny.
**Pierre Tessier** 22:34 Because I could see a lot of people doing docker compose, build, and then just naming a service or 2. And if you have to add profile. It's gonna break their workflows a little bit, and it's gonna it's gonna cost them
some angst.
**Juliano Costa | Datadog** 22:46 Okay, yeah. But I also feel that yep, follow up question that, should I do everything on one single pr, or
I do one thing, and then we do have a follow up.
**Pierre Tessier** 22:58 Let's add the Kafka. Let's add the checkout service variable 1st to respect this use Kafka, yes or no type of environment variable. And then let's do a Pr. To make it go. Profiles.
**Juliano Costa | Datadog** 23:08 Okay. I'll add that to myself.
**Pierre Tessier** 23:21 I could also say I'm starting to get less busy with my day job.
I had to hire 2 people, and I just made another hire yesterday. So that was.
**Juliano Costa | Datadog** 23:29 Awesome.
**Pierre Tessier** 23:30 So of course there's some onboarding that comes with that. But I I could. It's, you know.
You know. Yeah, it's
I. I'm having fewer things to that. Take up my time, but I feel I'll be less busy. So I'm trying to get that. So.
**Juliano Costa | Datadog** 23:51 But Lombardy is easy. The open telemetry docs are great.
**Pierre Tessier** 23:56 I'm trying to get some AI tooling in place. So so open tellmetry just we have Kappa now for the docs.
I I'm it's a really phenomenal tool.
I like to use it for our it helps with onboarding. I'll just leave to that
appa definitely helps for onboarding but it's it's more than just that. Right, Juliana. I'm sure you've you've recognized that
you gotta learn a whole entire platform of systems.
It it. I hired 2 people. I had to write a whole. We had to redo all our onboarding docs. We're growing as an organization. We're we're, we're. We've made several changes. And part of those changes is just how we do enablement. So I had to catch up on all that.
This is all for me to say. I am seeing my hours in the future starting to unlock better.
which will allow me to come back in here and look at things a little bit more attentively, so.
**Juliano Costa | Datadog** 24:49 Cool.
Yeah, I I think I think in Europe people are all on holidays now. So.
**Pierre Tessier** 24:55 Yeah.
**Juliano Costa | Datadog** 24:56 Do not need to worry about that.
But yeah, it would be nice to to have you back.
**Pierre Tessier** 25:21 Okay, I will, for what's worth for Jaeger. I'm gonna go down the path of getting rid of the the sub chart
because trying to keep another project updated so we can move forward feels hard. I would rather us have more control.
and what I'll do is I will render their standard all in one.
and then I will convert that over to template files inside of our sub chart.
It'll require some upgrade docs to go along with it.
but I think that'll be the best, and I will not include in part of the components, because right now we have this component thing that contains all of the the services in the demo. I'm gonna have it be something separate from that
because this does require different services to be spun up.
But that's I think that's gonna be the angle I'm gonna go with here for Jaeger.
**Juliano Costa | Datadog** 26:22 Cool.
**Pierre Tessier** 26:29 and and reduce a footprint and open search again, if if you're like, hey, we could cut 500 MB if we stop persisting logs, or if there's a way to only keep the last 6 h of log or something like that, let's make that happen, please.
**Shenoy Pratik (AWS OpenSearch)** 26:45 Yeah, we do have a plugin. So we can make it easy. Yeah, it's not.
They can.
**Pierre Tessier** 26:50 If if it allows me to save memory, I will take that all day long, because right now the search starts up, and it's pretty low in memory, but as it gets used, its memory just continues to grow. So.
**Shenoy Pratik (AWS OpenSearch)** 27:01 Yeah, that would be good.
**Pierre Tessier** 27:03 To to contain that a little bit. And and you know, hey, maybe we could come up with a goal here of of dropping it down.
you know, I we also have additional Kafka expertise at honeycomb
that that and I've mentioned to them. Our problem with Kaka is just a pig.
and and it it doesn't nothing. It literally processed like a message a second, and we reduce Kafka's footprint as as well. Somehow. So I may be able to tap into that person's skills who understands a lot more about Kafka for us.
It's funny. I was just. I was literally talking about the footprint of the demo yesterday with a colleague about honeycomb.
So I'm an offsite. That's why I'm in a hotel room. But during our activity. We're talking about exactly this. I'm like, it's it's a pig, it's so large.
How do we? How do we reduce it from 6 GB to say 4 GB. Can we do that?
That it feels like it'd be amazing if we could.
Okay, anything else that's top of mind.
**Shenoy Pratik (AWS OpenSearch)** 28:13 I've got something I don't have the right bandwidth to work on it. But this was around, adding some auth on onward.
So we have these Ui endpoints for the website, the astronom shop, Grafana, and everything. For with envoy proxy. So did you ever think about adding auth basic auth layer there.
This coming to a personal problem when I deploy this on Ec, 2 on Aws side, I always get security warnings that there's no auth
on your endpoint, and it's publicly exposed and such. So it's just thinking, if you can add envoy, basic auth, everything. All of these are like secured with a authentication layer.
**Pierre Tessier** 29:01 So leverage envoys basic off capabilities. And then when you
hit it, you'll pass in basic off credentials each time.
**Shenoy Pratik (AWS OpenSearch)** 29:11 Even when I spin it up
I'll ask for credentials, and that's what it is. That's what is used by anwar.
That's what I was thinking.
**Pierre Tessier** 29:19 Why do we need to do this.
**Shenoy Pratik (AWS OpenSearch)** 29:21 This just so that the envoy endpoints are secure.
Usually, if I spin it up, and that's how I suppose everyone spins up who is not working on a local machine. Anyone who is deploying this on a remote machine. They'll have to expose this endpoint publicly, or if they're using some gateways with some private links, then it's a separate thing. But if it is just a remote machine and you're deploying this there, you need to give public access to your.
**Pierre Tessier** 29:51 When we do this through an ingress controller
like, that's how we do it on eks. For example, I I use the Al.
**Shenoy Pratik (AWS OpenSearch)** 29:58 Yes.
**Pierre Tessier** 29:58 Controller which creates the the Ssl.
Endpoints for me, and then routes everything. Non ssl. Internally.
**Shenoy Pratik (AWS OpenSearch)** 30:06 Yeah, that's that's the right way to do it. But I'm not sure if everyone does it that way.
Oh.
**Pierre Tessier** 30:15 Yeah, because people who don't expose it like that, you, you basically want to expose it. So we could do. Ssl, right.
is that what you're trying to get at.
But to do. Sso, you need certs, you need to self sign your search. It's not just off. It's about.
Yeah. This is, this is not verified like non verified
**Shenoy Pratik (AWS OpenSearch)** 30:34 Ssl, so just do https with basic auth. You don't need sorts exactly, because you're not deploying the endpoint itself with https. It's just the proxy layer which has auth.
**Pierre Tessier** 30:47 Yeah, yeah, I get it. But you would. You still need to cert like the client still needs to verify the cert against what the proxy exposes.
When it does this handshake.
If not, you'll get a red screen in chrome.
**Shenoy Pratik (AWS OpenSearch)** 31:02 Yes, that is true.
**Pierre Tessier** 31:05 So.
**Shenoy Pratik (AWS OpenSearch)** 31:06 Let me check it out.
Yeah, we should do.
Yeah, yeah.
**Pierre Tessier** 31:10 Docs. Maybe what we should do is provide better docs on how to spin up Ssl ingress controllers for the 3 public clouds, azure Aws and Google
and explain to people that if you deploy this locally it's not going to be secure. So you gotta tell chrome I I accept whatever.
And and and this might just be a docs thing.
But I I think it's beneficial for people to understand like, Hey these, this is built into all the other tooling. You just need to provide.
You know, now that you think about it, even for aws, you still have to tell aws your search.
because when I configure the ingress controller, one of the the annotations for aws is the cert arn that aws.
**Shenoy Pratik (AWS OpenSearch)** 31:51 You need to upload it. Yeah, you need to create one and then attach it.
**Pierre Tessier** 32:00 and yeah, because basic off just does authorization. But it doesn't do. Ssl.
**Shenoy Pratik (AWS OpenSearch)** 32:06 Yeah.
eventually, Ssl, should be the thing we do. But basic auth can be the 1st layer. But also I I agree Docs itself can help a lot.
**Pierre Tessier** 32:18 Yeah, yeah, this feels like a doc change.
And you should have permissions on that.
You're in the approvers team for the community, Demo. So you should be able to write docs for the the demo. And then Severn or I forgot Patricia. Is that the other person?
One of them will approve it.
Yeah, I think it's worth.
Because you're part of the Demo approvers team. It's
It's it works. If you came out from outside they would request one of us to approve it first.st
**Shenoy Pratik (AWS OpenSearch)** 32:53 Okay, got it?
**Pierre Tessier** 32:54 Yeah, so you could write docs is what is what I'm trying to say.
**Juliano Costa | Datadog** 33:01 By the way, Pierre, we are you, me Miko and Roger, we are now Admins, on the channel on the back channel, so.
**Pierre Tessier** 33:14 On the slack Channel.
**Juliano Costa | Datadog** 33:16 Yeah, on the on the Hotel Demo Governance, the private one that was.
**Pierre Tessier** 33:22 Happen.
**Juliano Costa | Datadog** 33:23 Yeah, that that was created by Carter, but with his Microsoft account, so nobody had access to it.
**Pierre Tessier** 33:31 My goodness.
**Juliano Costa | Datadog** 33:31 At all. Oh, my God!
**Pierre Tessier** 33:32 Ness.
**Juliano Costa | Datadog** 33:33 I reached out to the guys from Cncf and said, Hey, can someone make me an admin here?
I need to kick some people out of this channel?
**Pierre Tessier** 33:44 Is Carter still at Microsoft.
**Juliano Costa | Datadog** 33:46 No, he he left like while he was still on the on the demo thing yeah.
So he went to lightstep, wasn't, wasn't it? And then, like.
**Pierre Tessier** 33:58 I heard lightstep is is getting shut down.
**Juliano Costa | Datadog** 34:01 Yeah.
**Pierre Tessier** 34:02 So I heard. I don't know if it's how true that is.
**Juliano Costa | Datadog** 34:07 Well, just like.
**Pierre Tessier** 34:08 Beside a little bit.
**Juliano Costa | Datadog** 34:09 Exist. It isn't service.
**Pierre Tessier** 34:11 Service.
**Juliano Costa | Datadog** 34:12 Oh, observability, something.
**Pierre Tessier** 34:14 Yeah, I believe they are. There might be changes going on there. At least, that's that's what I was. I'm spreading rumors. I should stop doing that, please.
**Juliano Costa | Datadog** 34:23 Well, I know that Adriana left
**Pierre Tessier** 34:26 Yeah, she's at the dynatrace now, isn't she?
**Juliano Costa | Datadog** 34:29 Yeah, so.
**Pierre Tessier** 34:32 Yeah. I still like her Linkedin post.
**Juliano Costa | Datadog** 34:39 I don't know.
Okay, cool.
**Pierre Tessier** 34:44 I will get looking at this. It will not be until next week. Sometime. I I'm going on Pto. Here in a couple of hours
through the remainder of the week. But next week I will take a harder look at Jaeger and for what it's worth. We should probably talk about getting a release out.
**Juliano Costa | Datadog** 35:00 Yeah, so on that unless you just text on the on the community, Demo Channel, saying that he will have a Pr for flex dui over the weekend.
**Pierre Tessier** 35:13 I've seen that, and I liked it with the party. Blob.
**Juliano Costa | Datadog** 35:15 Yeah, so maybe we should just wait and and.
**Pierre Tessier** 35:19 As as soon as that rolls out, I think we should do a we should cut a release is what I'm saying. It seems pretty pretty big for us to cut a release against, and it'll give us an Erlang
interface, which mean you can't read. But well,
Well, we have Gen. AI to help us.
**Shenoy Pratik (AWS OpenSearch)** 35:39 Sure.
**Pierre Tessier** 35:39 Okay.
**Juliano Costa | Datadog** 35:40 Jesus Christ. I have a thread with him, and and he was like, Oh, every time I look at airline code I'm like excited, and I'm like
I'm not. But.
**Pierre Tessier** 35:51 Thank you.
Going on here.
right now, hey? I'm about to not renew my intellij subscription, and I'm gonna instead use cursor moving forward.
I've been using cursor a lot more lately with good success at least.
So
given. You know, the demo is a lot of things, and it's hard to be deep in all the things. It's very wide. The demo, I think cursor, is very
helpful.
**Juliano Costa | Datadog** 36:24 Yeah.
**Pierre Tessier** 36:25 And it. It's great that it's not a production. So we can break stuff.
**Juliano Costa | Datadog** 36:30 It's not.
**Pierre Tessier** 36:31 Yeah, yeah, it's fair.
**Juliano Costa | Datadog** 36:32 Fair.
**Pierre Tessier** 36:34 But yeah, a honeycomb. We bought licenses of precursor for anybody who raises their hand.
So yeah, I also have.
I work on the Hotel Demo. I need AI to help me write Demos.
**Juliano Costa | Datadog** 36:46 Nice cool guys. So the the next Sig meeting I'll be out on Pto. But then the other one, I'll be back. So see you in a month.
**Pierre Tessier** 36:59 Yeah, I do need to run. Thanks. Y'all.
**Shenoy Pratik (AWS OpenSearch)** 37:02 Bye, bye.
