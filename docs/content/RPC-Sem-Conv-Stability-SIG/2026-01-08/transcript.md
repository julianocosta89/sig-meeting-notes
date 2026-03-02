SIG: RPC Sem Conv Stability SIG
Date: 2026-01-08
Duration: 46 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:19 Hello, hi Matthew, how are you?
**Matthew Hensley / Grafana Labs** 00:23 Hello.
Doing okay.
It's, gonna be an interesting one this evening, because I'm doing the single parent thing tonight, partner's out, and…
I have to get a kid to bed, so… We're gonna make it work.
**Liudmila Molkova** 00:42 Good luck with that.
**Trask Stalnaker** 00:43 Yes.
**Liudmila Molkova** 00:46 Thank you for joining.
**Trask Stalnaker** 00:47 We will understand if you watch the video.
**Matthew Hensley / Grafana Labs** 00:52 No, no, he's not even close to being settled down.
Plenty of time.
**Liudmila Molkova** 01:05 Mine are never closed.
Okay, so what do we have going on in the RPC world? We have a few things… In progress…
This is in progress through… This is in progress.
Okay.
**Trask Stalnaker** 01:36 I'm updating the migration guide based on the last two PRs to get merged.
**Liudmila Molkova** 01:45 Oh, nice.
**Steve Rao** 01:47 Hello?
I hope you do that.
**Liudmila Molkova** 01:51 Hi, Steve.
Okay, we… Don't have anything new?
**Trask Stalnaker** 02:09 So let's take a look at the… No, I think we're… I think we're winding down.
**Liudmila Molkova** 02:16 Yep.
Wow.
Before we… we probably still need to do some prototypes, update the existing instrumentations with,
**Trask Stalnaker** 02:26 Yes.
Mark it as RC.
**Liudmila Molkova** 02:31 Yeah.
So, I don't think there is anything to discuss here, right? The migration guide.
Just to update it.
**Trask Stalnaker** 02:41 Yeah.
**Liudmila Molkova** 02:44 Ayy.
**Trask Stalnaker** 02:46 Yeah, and maybe we can leave it open and target merging it when we… declare RC.
**Liudmila Molkova** 02:55 Right, or once it's merged, we would ask.
**Trask Stalnaker** 02:59 update it.
**Liudmila Molkova** 03:00 to update it to niche PR. Either way should work.
**Trask Stalnaker** 03:05 Yep.
**Liudmila Molkova** 03:08 Great, I have a small PR to review.
Oh… Steve, Matthew, if you could take a look, it's just make server address not required.
Because it's not always available, and it's currently required.
And there is… Yeah.
The… one of the things I want to discuss today is… What we do is… spend
Oh, thanks, you folks approved.
So…
**Trask Stalnaker** 03:51 I had to comment on your comment here, also.
**Liudmila Molkova** 03:54 Oh, nice.
**Trask Stalnaker** 04:00 So, in general, we've kind of… we've treated… When we go to stable…
We have done the bump of things that still weren't stable yet at that time.
Under the idea that, hey, we're taking a breaking change, we may as well sync up to the latest spec.
But I think
We could make a different argument for span events versus events if we want to, given that it's part of a entirely orthogonal
Migration effort.
**Liudmila Molkova** 04:43 Mmm.
Yeah.
**Trask Stalnaker** 04:45 So, I kinda tend to agree with you on…
Not making it part of this.
the RPC migration, since… We… Still are kind of working out that other migration…
**Liudmila Molkova** 05:06 Right, so what we would do here is… We would towel…
Instrumentations.
That already meet those. What we want them to do is to keep doing whatever they're doing.
And not migrate.
At all.
And if they are doing this future stable RPC, they should not Enidos.
In the stable version at all.
For the new conventions.
**Trask Stalnaker** 05:55 Do we need to say… like, I remember we're just wondering, like, if we don't say anything at all here, we just call them events, right?
In semantic conventions.
And we've sort of… We don't actually see… We've sort of said that people use…
Like, we haven't really finished that story.
Yet.
Are we expecting… well, I guess we have, kind of, because we are asking for, like, GenAI folks to start using log-based events.
In order to get complex attributes.
**Liudmila Molkova** 06:41 The Gen AI is…
Okay, so when we… in GenEI, when we are defining these events, we are defining them, assuming they are, like, independent.
They're useful, maybe even without a spin.
These things are completely useless without a span.
And we That's fun.
**Trask Stalnaker** 07:04 deprecate this?
Yes.
I would support that.
**Liudmila Molkova** 07:12 Yeah.
So, if we deprecate it.
things, I think, become clearer, because we don't want somebody to start emitting those as log-based, or to start emitting them at
Oh.
**Trask Stalnaker** 07:30 Yeah.
**Matthew Hensley / Grafana Labs** 07:30 I'd say doing that, and adding a note that the intention here is they'll be added back in the future once
The other spec is settled.
Or, you know, whatever…
gets done, but there's a reason it was explaining why it was deprecated. I think that would,
Make implementations a lot.
More straightforward, fewer decisions to make.
Go straight for the spec.
**Trask Stalnaker** 08:01 Are people using… This…
**Liudmila Molkova** 08:07 Java emits them. I don't know if they're using them.
If somebody is using them.
**Trask Stalnaker** 08:15 Did we turn them off by default?
**Liudmila Molkova** 08:20 Oh, it's strange.
**Trask Stalnaker** 08:35 GRP.
Hmm… We do have it behind a condition.
Omit, But the default is true, to omit them. Okay.
**Liudmila Molkova** 09:12 oh, by the way, you, you, I think you emit, with different name.
It's not even the same name, it's just message.
Yeah.
And, in some countries have our PC.message.
Fun.
Yeah.
**Trask Stalnaker** 09:34 I think in our distro, we suppressed those, because they were noisy.
**Liudmila Molkova** 09:43 So, the current spec…
**Trask Stalnaker** 09:47 Cease to emit them for unary calls as well, which makes…
**Liudmila Molkova** 09:53 Little sense at all.
**Trask Stalnaker** 09:56 Right.
**Liudmila Molkova** 10:01 Okay, so if we deprecate them…
Essentially means that whatever you're doing, keep doing it, don't start doing it from now on. And maybe in the future, we will resurrect it.
If we… if we want to do something better for streaming.
**Trask Stalnaker** 10:26 I tip… I hesitate to dep… so, deprecating… To me, means…
I mean, if we made your version bumped Java, we would…
Drop it, if it's been deprecated.
**Liudmila Molkova** 10:51 Yeah, so if somebody uses it, they will have no… Us.
Herbert.
But it's a major version bump.
**Trask Stalnaker** 11:09 Yeah.
I mean, we… we can.
So do we think we're going to bring these? But we think we would bring it back.
as logs.
**Liudmila Molkova** 11:35 So ideally, I think, We'd rather… Ask.
Somebody who uses streaming.
to report custom… Spence.
They would… If they care about the duration, they would create a span, And… For each individual message.
**Trask Stalnaker** 12:07 So you're… I mean, I… I'm… I'm okay with… dropping them…
Personally, I think I haven't personally seen them being useful.
I guess, so that's… that's my question, kind of, to the group, is… Do… Have other people seen…
use, these… being useful.
**Matthew Hensley / Grafana Labs** 12:49 I'm looking at the… NET WCF instrumentation to see if they're admitted.
Do you know the GRPC?
Tracing spec that we looked at.
per… The Christmas holiday.
Does have quite a few events, but… It's never been implemented.
Over on.
On gRBC stuff, so…
**Liudmila Molkova** 13:15 I think it's been implemented, and they have way more of them.
Let me… shh…
**Trask Stalnaker** 13:25 Oh, I thought they only did metrics.
**Liudmila Molkova** 13:28 They did tracing, Show that… Sorry.
**Steve Rao** 13:40 Java instrumentation.
**Liudmila Molkova** 13:42 Yeah, I, I went to…
Looking for the gRPC spec that talks about tracing.
**Trask Stalnaker** 13:53 A66 is the one about metrics.
**Liudmila Molkova** 13:59 Oh, A72, thank you.
So, they, they have quite a few events.
Year.
They do it a little bit differently.
So they report some load balancing stuff in Java.
they have…
It's… it's kind of messy.
They report maybe two events?
One is for compressed, one is for uncompressed, because…
This is probably… there are some API limitations around this.
I don't know how useful it is at all.
**Trask Stalnaker** 14:59 Probably all came from Open Census. That's probably where we got our… our PC… some cons.
Mess… that message event.
**Liudmila Molkova** 15:13 Oh, that's a great point.
Yeah.
**Trask Stalnaker** 15:19 Not sure how that helps us.
Except that…
Probably some people.
Did… do… use it, or at least Google, at least Google, internally, probably uses it.
**Liudmila Molkova** 15:38 Let's say somebody needs them. Let's say we deprecate them, and somebody needs them.
They would come and tell us.
And we will add them.
Or they will let them.
**Trask Stalnaker** 15:53 Yeah.
I think it's a reasonable, that we say that as part of stabilization… were… Dropping it.
But… We're open to bringing it back as log-based events.
**Liudmila Molkova** 16:16 Right, and at that time, we probably should think about
What is the… what content of this… this event… how… how they should be expanded, if expanded at all.
To be useful without spans.
**Trask Stalnaker** 16:37 Yeah, I will, I will…
ping, Java folks, and also potentially maybe OTEL maintainers.
To ask if any, you know, to share that proposal.
Odd. Mmm.
just to… In case there's any…
Buddy who will be upset by that.
**Liudmila Molkova** 17:52 this would also be on our plate, too, once spent events are deprecated to find out.
**Trask Stalnaker** 18:00 Yeah, I mean, I kind of feel like we can… An option for us.
If we want to kind of punt it, is just to…
Remove the warning from the top of this page, and…
just kind of merge it as is. You didn't really change anything here, where RPC SEMCOM doesn't…
Like, we'd already essentially changed, removed span events.
from… independently of the RPC stabilization effort.
**Liudmila Molkova** 18:43 Yeah, and I… I…
I agree. Let's try to figure it out. If you want to ping hotel maintainers, go ahead. If you'd rather me ping you, I can also do this. The reason I stumbled upon it, I've tried to document the mapping between
GRPC and OTEL.
And I realized I don't want… I cannot be as specific as I want to when I talk about the mapping for this.
events.
**Trask Stalnaker** 19:11 Oh, I see.
Oh, interesting. So there was some, some… differences?
**Liudmila Molkova** 19:25 Yeah, we can switch to the mapping. Yeah.
Okay.
So… I think I didn't edit the agenda, but…
It's in draft still. I wrote it before holidays, and I re-read it, and I think there need to be some changes, but…
This is the mapping.
For metrics, This is the metric attributes, the GRPC sets and the hotel sets.
And this is conversion.
In both directions.
And for metrics, it looks… reasonably good.
These two friends are pretty much the same.
Those differences are the same.
gRPC target is pretty much server address and port, with caveats.
So, the gRPC target string… It's actually the… Custom 1.
was additional DNS resolution.
So this is, like, the regular one.
this.
Means that this is the…
base name, and then there is a custom resolver that would expand it into multiple, maybe, original endpoints.
Where… Hedging endpoints or something.
Multiple shirts. And we have means to record address and port.
We have no means to record… well, we have Euro scheme, but we… we don't record it on the…
Rbc.
**Trask Stalnaker** 21:30 Yeah, and is it really… Is it really URL scheme?
**Liudmila Molkova** 21:36 It's… Actually, this is URL scheme. This is not the authority, though.
Authority is empty. This is a pass.
**Trask Stalnaker** 21:47 Yeah, that's why I'm confused.
The extra slashes, okay.
**Liudmila Molkova** 21:55 This is a valid URL, but without authority.
**Trask Stalnaker** 21:59 And the thing that looks like a server address is not…
a server address. It's in the… well… It's in the past.
**Liudmila Molkova** 22:10 Yeah.
**Trask Stalnaker** 22:12 If you parsed it as a URL.
**Liudmila Molkova** 22:15 Right. There is a deterministic algorithm that allows you to
Get the server address and port from it.
**Trask Stalnaker** 22:24 Okay.
**Liudmila Molkova** 22:28 So what it means, that this conversion is the rate forward.
**Trask Stalnaker** 22:36 The opposite one.
**Liudmila Molkova** 22:39 is reasonable, but lossy. You would…
If you originally had something like this.
What you would see is just this, you wouldn't know.
That there is some custom… Name resolution.
I think it's… Kinda reasonable.
**Trask Stalnaker** 23:05 I mean, we can… we could definitely… add gRPC.target.
As a… an attribute.
**Liudmila Molkova** 23:23 We could.
With it.
been necessary?
**Trask Stalnaker** 23:35 I don't know how important That piece of information is…
Do you know…
Go ahead.
**Liudmila Molkova** 24:06 We could add Euro scheme.
If it's available.
**Trask Stalnaker** 24:14 How… would that cover, like, Unix domain socket?
**Liudmila Molkova** 24:23 For Unix domain, we would still have the… The run spurt.
Great,
We have the transport, which… would be… You… Unix, I think?
Oh, no, we wouldn't.
Oh, yes, it would be Unix.
**Trask Stalnaker** 25:15 But then where does the rest of that… path, go.
the right leaks.
**Liudmila Molkova** 25:27 Server address?
**Trask Stalnaker** 25:29 Yeah.
Oh, that would be server address?
**Liudmila Molkova** 25:35 Yes, server address is… One of the possible values, or…
Sorry.
Unix Domain Socket is one of the possible Wally-ish?
**Trask Stalnaker** 25:50 Oh, it is. Okay.
**Liudmila Molkova** 25:56 Okay.
**Trask Stalnaker** 25:57 Okay. Yeah, yeah. No, you… that convinces me.
So, all that were… yeah, because I was thinking we were missing more than just the scheme, but if we're only missing the scheme.
Then yeah, we could definitely capture… God… URL.Scheme… to the gRPC… semantic conventions.
**Liudmila Molkova** 26:29 Okay, so let me create an issue for this…
Okay, wonderful.
The metrics become… fully comp… Hat, but we can… we can preserve the same information.
This one is 3VL.
this one… we would… need to use custom logic, because for… gRPC doesn't populate, it will just…
decide based on the GRPCS status.
So these are the two metrics that are compatible. This is the GRPC version, this is OTEL version.
One for client.
One for server.
Dar… A few metrics that your PC has that don't have mapping?
**Trask Stalnaker** 28:27 The one's for attempts.
**Liudmila Molkova** 28:31 And… The things they have for… Compressed message size, and uncom…
There are 4 of them. Client, server, sent, received.
So, ours are completely different.
Hours are per request.
So the total is not the network's throughput, because if there are retries, we don't account for retries.
Oh, plus we at least document that it's uncompressed size, but how do we know it's uncompressed size? I don't know.
I think we don't know when it's uncompressed.
I think those are completely useless, and I…
I, I wish we didn't have them.
**Trask Stalnaker** 29:37 deprecate them.
**Liudmila Molkova** 29:44 Yeah.
**Trask Stalnaker** 29:46 I mean, I kind of agree, like, it's almost better to…
Deprecate them than to leave them around in…
A confusing state, because people will… Attempt to implement them.
Just… to follow the spec.
**Liudmila Molkova** 30:13 Yeah.
And the other motivation, if it's just the network's throughput.
Does it… does it have to be RPC-specific?
That, that, that's… that's the hard discussion. Anyway… But…
Create this issue, we'll think about it more.
Yet again, I've lost my pull request.
Okay, so this, in broad strokes, are metrics.
spans, or… In a similar shape, but with slightly more fun.
So, gRPC spends…
**Trask Stalnaker** 32:39 Have slightly different spend naming.
**Liudmila Molkova** 32:42 Which is 3VL to convert.
The spam status code… They simply say that everything is not… that's not okay is an error.
We are a little bit more specific.
But it's still… doable.
to convert.
There's… there's caveats. Spence status description… so the only place the status code appears in gRPC spense is inside status description.
And it appears as a string, like… Like this.
It's a standard form.
**Trask Stalnaker** 33:22 Oh, so they have status on the metric, but not on the span?
**Liudmila Molkova** 33:28 They don't have any, any… Attributes on the spend itself.
**Trask Stalnaker** 33:32 Oh, interesting. Okay, okay.
**Liudmila Molkova** 33:36 So, it's… Probably possible to convert spans back and forth.
There is no means to populate any of the server network attributes.
But it… Still, the conversion back and forth.
Kinda works.
**Trask Stalnaker** 34:04 Yeah, and I… I don't… Do we need…
To… is the goal to be able to… I guess…
I guess so, yeah. I guess that just makes sense. I was gonna question whether the goal was to be able to have
Like, really a precise mapping… Like, who would use that, but I guess, like, a back-end…
or somebody who is consuming both gRPC-native telemetry and open telemetry SEMCON.
It would be nice to… convert.
I would say gRPC2… OpenTelemetry semantic conventions would be the priority.
**Liudmila Molkova** 35:04 Yeah. I don't think we need a precise mapping, and that should be a blocker to anything, but I wanted to make sure we
Documented as precisely as possible.
And that, for example, here, it became obvious that none of this should be absolutely required.
**Trask Stalnaker** 35:26 yeah, yeah.
**Liudmila Molkova** 35:28 Nice. Yeah.
But…
I don't think anybody would use it for SPAN specifically, because they are experimental and opt-in on your PC itself, and if…
My impression is they… it would be okay for even for Google to break the compatibility.
Dear.
Okay, so the last, but not the least, is the span events. This is just for the completeness.
**Trask Stalnaker** 36:06 IS.
**Liudmila Molkova** 36:07 So they, they have some span events for load balancing, And…
So, I'm seeing here that if you…
If somebody wants to do the conversion.
We would rather ask them to just preserve.
this.
as… Pan event.
Alternatively, we don't need to specify it.
Since we don't target the full… compatibility.
**Trask Stalnaker** 37:01 And since we're not stabilizing… those…
**Liudmila Molkova** 37:06 Yeah. Power.
**Trask Stalnaker** 37:08 event.
**Liudmila Molkova** 37:11 So we can just say that span events go as is.
For as long as Hotel supports venements.
**Trask Stalnaker** 37:25 I mean, you would…
This would be just events.
I mean, we could map events…
I think the question 3 comes back to what are we… what do we want to do with
the gRPC, or the RPC… events in STEMCons.
**Liudmila Molkova** 37:52 So if we apply now the scenario of deprecation, then we see that the current ones are spine events, because this is the current practice.
And future, there's… None.
**Trask Stalnaker** 38:06 Do we even need to say that they're span events? I mean… Versus events at…
I thought we were trying in semantic conventions to to… just say events… And… Imply log… imply… log-based…
but also support SPAN events.
And for it.
**Liudmila Molkova** 38:41 Since we don't want anybody to implement them.
**Trask Stalnaker** 38:44 At all?
**Liudmila Molkova** 38:45 I'm fine… being very ambiguous, and just, just default to events, whatever it means in semester.
**Trask Stalnaker** 38:53 Yeah.
**Liudmila Molkova** 38:53 interventions.
**Trask Stalnaker** 38:55 Yeah.
I would be fine if somebody implemented them using log-based events or spanned events, I don't…
**Liudmila Molkova** 39:09 As long as they don't make it stable.
**Trask Stalnaker** 39:13 Yes.
**Liudmila Molkova** 39:21 So, perhaps this becomes…
**Trask Stalnaker** 40:13 Yeah, I like it.
**Liudmila Molkova** 40:17 Okay.
Cool.
Then I'll just remove this. I…
This… this doesn't benefit anybody. There is no compatibility between those two friends, the gRPC and Attel, it's just, makes no sense to convert anyways.
**Trask Stalnaker** 40:39 I'm… Super good with that.
**Liudmila Molkova** 40:46 Okay.
So then I think we are… discussed everything.
**Trask Stalnaker** 40:59 Alright, do we have anything on the to-do that is not already in progress?
**Liudmila Molkova** 41:10 Yeah, there are a couple…
This… there's nothing to tackle, right? For… This one.
I've been… Looking… To what we can do there.
And… I… Don't think there is anything we need to do.
So, when we…
Talk about… the status.
Oh, sorry, this is metric.
When we talk about status.
It's a… We're referred to the general guidance.
Which says… that… Well, it depends on the context.
consolation… If you know… It's… it's… it's okay. It's not a failure.
Don't record it as a failure. If you don't know, It's a failure.
**Trask Stalnaker** 42:37 What do we current, because gRPC has a cancel status.
Does it have a cancel status code?
**Liudmila Molkova** 42:46 It does.
**Trask Stalnaker** 42:48 We are currently… Mapping that to OK.
I assume…
**Liudmila Molkova** 43:01 Change number 4?
Maybe status quo… Okay, so on the client, everything but okay is an error.
on the server…
Only those are errors.
And consolation is not one of them.
Think?
This is… consistent with HTTP?
Where we consider consolation and error on the client.
And it's so…
**Trask Stalnaker** 43:57 Moon, snow, is… is there any… there's no… Cancellation code… on HTTP.
**Liudmila Molkova** 44:10 The… Whoa.
It depends on the language, right? Let's say in .NET, it would… the cancellation would result in exception.
Yeah. In Java Reactor, it's… the middle ground.
The timeout is also a cancellation.
To some extent.
**Trask Stalnaker** 44:34 Yeah, I guess if we… for gRPC,
Do… does cancellation occur on timeout?
Or is timeout is a different status.
Because if cancellation is only something that
You proactively cancel because you got something else, or you decided you don't need it anymore.
**Liudmila Molkova** 45:04 Okay, so what you're saying, that we could…
Revisit the list of error codes on the client.
And maybe at consolation there.
**Trask Stalnaker** 45:19 Yeah… When a gRPC client is no longer interested in the result of an RPC call, it may cancel.
Deadline expiration and I.O. errors also trigger cancellation. Oh, awesome. Okay.
Okay.
Well, anyway, we hit time. That's more complicated than I was hoping.
**Liudmila Molkova** 45:49 Yeah.
But if you think about something that we can do on this issue, yeah, let's do it.
**Trask Stalnaker** 45:57 Cool.
Alright.
**Steve Rao** 46:00 Okay.
**Trask Stalnaker** 46:00 Great progress.
**Liudmila Molkova** 46:03 Yeah, thank you all.
**Steve Rao** 46:05 Yeah, present to you, bye.
**Trask Stalnaker** 46:06 Yay…
