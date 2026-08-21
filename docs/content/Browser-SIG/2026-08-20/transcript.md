SIG: Browser SIG
Date: 2026-08-20
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Jared Freeze (Embrace)** 01:36 Hey, dude.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:40 Hi, Jared, how are you?
Bye, David.
**Jared Freeze (Embrace)** 01:43 What's up?
Do you want me to drive to them?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:49 I can, I can do it.
**Jared Freeze (Embrace)** 01:51 Okay.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 02:08 Yeah, Wolfgang.
**Jared Freeze (Embrace)** 02:10 It worked.
**Wolfgang Therrien** 02:12 Hello, everyone.
**Joaquín Díaz** 02:15 I hope.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 02:18 They're welcome.
I'm just gonna wait one more minute to see if anyone else joins.
Okay, let's… let's get started.
Okay, so we have three things to talk about, David. You have the first one, looks like just a… Request for review, do you want to talk about this?
**David Luna Bistuer** 03:49 Yeah, well, there are a lot of finishing touches in the HHR, the implementation. I think I already got a comment from Jared about the… one of the configurations of applying.
custom attributes, but I think this is part of another conversation about configuration.
But, please review, already got Joaquin, thanks for the review and the approval.
So wait till next week to… to give enough time to anyone else to… if you want to review. But basically, it's the same.
So we are installing a LCHR API, the prototype, open and send.
We decided, I think it was last week, we decided to start a spam open send instead of open, because something might happen in the middle.
And then I'm using the same mechanism for, get resource timings, correlated to the span.
Okay, and also, something that was different from the former, instrumentation is that the error handling was different, now it's the same. So, tests from Fetch and XHR have similar, error handling right now.
So, yeah, long story short, so that's the TLDR.
happy to get more reviews, and hopefully with this, I think… There is an issue about removing webpage provider, I think that would be something that… Well, the last item, too.
have when… if we have this information already in the browser repo, we can see that we removed, any trace of the web tracer provider and the traces web package.
Okay, so thank you very much.
**Jared Freeze (Embrace)** 05:34 Okay, cool. I did have one comment. I thought of something. We were dealing with this at Embrace, where… there's… So, the way that the XHR works, right, you have two functions, which is sort of why we were talking about unwrap, not unwrap. So, my idea was that, because it's synchronous.
You could do a tri-cut for open.
Like, for the… for the, you know, when you override.
Then, immediately… so if it… if it fails, immediately flip it back to original and just exit.
Then do a try-catch on send, and again, if that fails, undo both, and then exit.
So that… I feel like that kind of is the best of both worlds, because nothing can sneak into the frame in between, like, from another vendor, which is what that garden was for.
So, I think, if I'm… Not totally off-base here, I don't think anything can sneak between those two calls, And then that might solve our problem of this sort of, like, oh, well, if it fails on open, just exit and you're good, like, fetch, right?
So, I don't know if that's worth trying. I'm not even sure how to test it, really, but…
**David Luna Bistuer** 06:45 Now I remember the conversation. So yeah, that was another conversation we had, that, since we are patching two things, We… well, the first implementation was… wasn't wrapping them.
But as Jared said, maybe it's a bad idea, because we were… we were messing with the… with that.
But there was a situation if we could patch open but not send, and we tried to enable many times the same internalization by patching and patching and patching and patching again, so we get, A big stack of function calls that actually they're doing the same. Well, just one thing.
So, yeah, I think they're right. I think that it's because that's synchronous, it should work on the same frame.
Then it shouldn't… it shouldn't… we could… we could do this individually, and then… Yeah. Just… reset everything up.
**Jared Freeze (Embrace)** 07:36 Because I think right now, it guards on enabled, right? But really, we should just have another variable that just says, like, we tried.
Like, we tried already, like, not… not just my enabled.
**David Luna Bistuer** 07:46 Doesn't.
**Jared Freeze (Embrace)** 07:46 and, like, just keep, you know, yeah, I love cycling, so…
**David Luna Bistuer** 07:50 Okay, I'll, I can, I can apply those changes in the, in the current PR, and… I'll have a final review from you.
Thank you, thank you for reminding me this.
That's…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 08:06 Alright, next topic, Joaquin.
**Joaquín Díaz** 08:11 Certainly, like, thanks, Davis, for working on the fetch instrumentation, I did that.
I added, like, an internal migration that tests So, an internal test attest to migration.
And it's basically running both the old instrumentation, the new instrumentation, comparing the spans, and trying to match them together.
It's just a way of getting more confidence of deprecating the old instrumentation.
And, like, a place to put test cases that, in case we find some inconsistencies with the old and the new one, we can put it in there, so we don't forget.
And it also kind of documents the differences between the two of them, mostly around, error funding. Again, like.
the OS limitations were not really… 100% some of the Commission's compliance around tests… oh, sorry, around errors.
Mostly around, I think, is status quo. That shouldn't be said on certain occasions on the error type.
So anyways, it's all there, documented, at least also testing whatever needs so much.
So, if you can take a look, that would be great. And then, ideally, we can do the same for XHR once that's merged.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 09:32 Sounds good, thanks for doing that.
**David Luna Bistuer** 09:34 Do you think, question, do you think after that, maybe you could set, put something in the red map to say, okay, Well, some information about the migration, and then point to these tests.
So people can look and then do the comparison?
**Joaquín Díaz** 09:48 Yeah, I think we should have some migration guide, like, stop importing from this package, just it's your package.
these are the differences that you won't see as part events, you won't see, all these parts, you will see the logs as the resource assignments, stuff like that, and, like, the things we actually fix, in regards to semantic conventions. I think we should have some README file, and then, yeah, we can point to that.
But maybe we can wait until everything is merged, so we have, like, a site base to write the documentation from.
And then we can, yeah, we should add that.
**David Luna Bistuer** 10:27 Okay, thank you.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 10:33 Okay, sounds good. So I have, I have the next topic, So I've been working on, looking at, the semantic conventions Registry.
I'm not gonna share my screen.
So, I did open this kind of high level.
Issue yesterday, which was essentially… Kind of mirroring what Android has done.
So, this is proposing having, our own semantic convention registry here in our repo.
And which has a dependency on the core semantic conventions, and… It would, also, if we… if you do end up having Client-side registry, it would have a dependency on that as well.
So Android has already done this, so I'm kind of just following what they've done.
I think this makes sense, because… Because there will be some attributes or some conventions that, are browser-specific, and also, like, this gives us, kind of, tooling. Like, part of this effort is tooling to actually, actually generate, constants from, the registries.
So they're not hard-coded in the instrumentations.
So this… this is kind of proposing to do it in sequence, so… First, first would be just documenting what we generate, and then add tooling.
Then switch, update the instrumentations to use the, the actually generated, constants.
And some, some checks, MCI as well, so… Yeah, take a look at this to see if I missed anything. I also started by… Opening a PR for the first step, so this is… This essentially adds… as a SIMCAN folder with some YAML files, which is… following the same pattern as in the semantic conventions repository, so all… all of the things that I, so I haven't done any, any, like… It hasn't done any changes to, this… this PR just basically reflects what we… should reflect what we generate today.
So it's got, all of the events that we generate with their names, and with all the attributes that they generate.
There's also a registry of all the attributes.
Yeah, so… hopefully… hopefully this looks good. Take a look at this as well. It should just mirror what we already have.
And then I think we can keep working on this. If there is any inconsistencies or any duplication, then, like, we can, like, continue working on this registry. And after this, we can also work on the tooling.
Yeah.
Any questions or comments?
**Jared Freeze (Embrace)** 13:49 Thanks for doing it. This is awesome.
**Wolfgang Therrien** 13:51 Yeah. I think this is sort of in line with what the GenAI, you know, folks have done too, like, breaking out the semantic convention separately for GenAI so that can… they can be iterated on at a… Faster, and released separately.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 14:08 Yes, that's correct, yeah.
**Joaquín Díaz** 14:13 That'd be…
**Wolfgang Therrien** 14:13 super excited.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 14:16 Yeah, and the semantic conventions Contributing Guide actually does recommend that, like, components that have Their own specific conventions, like, can document it in their own repositories.
So… Yeah.
**Joaquín Díaz** 14:34 Quick question. First, I really like this because it lets us… iterate way quicker than having to go through a simple visuals PR.
My main concern will be… Hey, good night.
We are always trying to use… Or trying to share as much as we can on guide-side conventions, like… making sure we are not doing something that may apply to mobile on our own repo. I guess that's something we just have to be careful about. I don't think there's nothing that we have to change about, like, this issue that you're describing here, but just something to have in mind.
And then, are we going to do, like, a separate… release process for the conventions, like… So… This is something that we've actually been talking other ways recently. Like, what happens if you change an attribute?
Thus… Like, does mean that you are doing, like, a breaking change in terms of December?
or it's not, because it's not an API change, per se, it's just you are changing… whether adding or removing an attribute.
So I guess, yeah, I guess I would want to know, or we can discuss that later, how we're going to version this, like, whether we're going to have, like, our, Browser CENCOM version, and then we will point that from the SDK.
And then what happens if that changes? Like, do we have to make a break-in, or a new version of the SDK as a breaking change?
which, again, all this applies to today's process, right? Because this just changes where these files are located, but… Right now, today, if something changes on the current semantic convention repo, like, are we doing a… are we tagging it as a breaking change on our own repo or not?
Yeah, I don't think we've discussed that, and this reminds me on that.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 16:44 Yeah, so, as far as, like, the… the, overlap between the different, the core semantic conventions, and if there is also one that we share with the, mobile, I think that's a… that's a… that's definitely, Something that we need to, keep an eye on it, and it's also what, I actually went to the Semantic Convention's SIG this Monday, and… That… that's… that's their main concern as well, kind of just us going off and doing our own thing, and never, like… you know, communicating with the core semantic group, semantic conventions group.
So their ask was that, like, we do have, representation, you know, in the semantic conventions SIG.
So I… I'm happy to do that, but I… sometime, but it would be good, good, like, if… if some of you would participate in that SIG call, at least occasionally.
**Joaquín Díaz** 17:51 Yeah. You want to set up, like, a rotation? I'll be fine with that. Yeah. Like, we can do… one, like, Each person takes one week, and then we rotate.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 18:03 Yeah, yeah, we could do that, yeah.
**Jared Freeze (Embrace)** 18:06 I'm wondering if we should just go through the client-side SIG.
like, if that's enough to, you know, come to agreements and then let it bubble up from mobile, because I feel like they're super active, too.
So having… a lot of clients have people going to the Semantic Convention saying, totally fine, but it may be easier if we have a little less representation.
I, I don't know.
But, you know, that's where the agreements, I think, are gonna happen, so…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 18:36 That's true.
Like, once… once the… the shared client… client-side semantic conventions takes off, then I think it will probably shift, most of the conversations will probably shift over there.
For now… I think it's just, like, the main thing is just that, like, we have some kind of browser representation.
You know, there, so… But yeah, as far as the versioning, or, like, the braking changes, so… I… I do agree, like, there is… this manifest file, actually does have… This, Browser-specific schema, which is versioned.
So, like, the whole idea of these federated semantic conventions is that, we would have our own version schema.
I don't think anybody's actually doing that right now.
I'll have to check if the Gen AI is generating, or how… if they are, and how they are doing it, but that would be, like, a follow-up to this work, figuring out how to do the versioning.
**Wolfgang Therrien** 19:48 Trying to dig through the, the, the notes from the semantic invention SIG, I think right now there's an effort to maintain aligned version numbers.
But I'm having trouble finding the evidence of that. That should… so it's just like a… I'll see if I can find the actual evidence or discussion in Slack or in the, in the, in the notes there, but I think that's the direction That's really…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 20:18 Okay.
Yeah, I mean, so for now, this is just, this is better than the status quo that we have right now. And it's… once we have all the tooling together, then I think this would be a natural next step, like, figuring out how to do the versioning and the releases.
**David Luna Bistuer** 20:41 Okay, maybe another question. That means that we have now our own registry completely disconnected from the semestering ones?
From the original one, sorry.
For example, what about if the HCB semantic conventions change?
Is that reflected here? Is there a way to refer to that semantic conventions?
You mean, like, if some… Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 21:12 Yeah, so you mean if some semantical mentions that we use from the core register.
**David Luna Bistuer** 21:17 You know.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 21:18 change.
**David Luna Bistuer** 21:20 Yeah.
Is that maybe a part of the tooling that we have to sync with that?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 21:25 That would be part, yes, that would be part of the tooling, and it's actually described in this, I'm sorry.
**David Luna Bistuer** 21:32 Yeah. I hadn't had the chance to read, yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 21:35 So that would be, let's seek.
Yeah, so it's essentially… so we have… we declare, like, the version that we depend on, and if there's a new version, then, like, we would have, like, a CAI check that catches that.
And there is also… Weaver has… has, like, a validation step that can check, check, you know, compatibility.
**David Luna Bistuer** 22:04 Okay, makes sense. Okay, I'm happy… okay, I'll review it, and we're happy to happen with the tooling.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 22:11 Okay.
**Jared Freeze (Embrace)** 22:14 So I have a quick question. So, like, on line 26, that comes from HTTP. Is there a… Is there a… another key that's, like, this is Lynn?
Or this comes from somewhere else? Is that… or is that what this file is?
Is… is there a way to, like, say officially, like, go back to this URL for… Yeah, let's see… HTTP, or URL, or whatever.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 22:43 So… I'm getting up to speed with this myself, this… these ones, I think, so… Let me see, so this one is HTTP request.
Yeah, so… So… The registry is… this registry file is, like, our own attributes.
So if they're not in this registry AM file, then they would be coming from From the one that we depend on.
And again, like, the idea is that Weaver can do all this validation for us.
That's the best answer I have at the moment.
**Jared Freeze (Embrace)** 23:38 Okay, that's great. Yeah, I just… and I saw you have a URL at the top of that file as well, at spans.yaml?
Which is great. I'm just wondering if there's more, but we'll find out.
As we go.
**Joaquín Díaz** 23:52 Do we… do we need to define or redefine the ones that are shared?
like, the spans, like, I guess that's the network request span?
Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 24:10 Yeah.
**Joaquín Díaz** 24:11 Er.
like, my concern would be if… I guess if we were to get… take care of that, that's fine, but… If we deviate, or something potentially changes upstream about this one that is fair across all clients.
Yeah, they might… Chris, Idea about this will be that we only define what is browser-specific, and then we use the rest from upstream.
Unless we change something for the browser, which I don't think that's the case for network response.
So… yeah.
If we can, like… avoid having this one here, and just use upstream, that would be ideal, I think.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 24:58 Okay, yeah, let me double-check on that, like, I thought that, if we generate these, then… Would make sense to have them documented here, but… if he, like, if our instrumentation uses these, but maybe, maybe you're right, maybe we don't need this. I'll double-check on this,
**Joaquín Díaz** 25:14 Right, yeah, because we will use that, but we will use it from the core repo directly, right?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 25:38 Okay.
**Joaquín Díaz** 25:39 Like, if we have a span that we use, like, our own span, then we will have a spans file, but we just don't have, like, the network span.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 25:49 Yeah, yeah, yeah, makes sense.
I'll follow up on this.
**Wolfgang Therrien** 25:58 put a link in there related to the versioning, for GenAI. I think initially, we're… we're thinking, It's all coming sort of back to me now, but initial alignment, and then separate version, because all the GenAI stuff was originally in the core repo, and so I'm pulling all of that out.
I think there was a desire to have an initial alignment Okay. The issue's there for… for reading.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 26:28 Okay, I'll… I'll take a look at that, nice.
Alright, we've got 5 minutes left, and still 2 more topics, so really quick. Jared.
**Jared Freeze (Embrace)** 26:40 Yeah, mine'll be quick. So this is more in anticipation of needing help, but I wanted to put it out to, vendors that use four hotel airports in their tooling, that There's not currently, like, a latest tag in The core repo, or contribib.
As far as I know. But this is such a good change, that we're using linear exports keys, which means we can't do deep Imports, there's a lot of changes there. Cjs changes, like, the extensions are changing from .js to CJS.
there's a lot in it. I'm still trying to figure out if I can't get a latest tag in the core repo through CI, I'll probably have a fork, which may be a little bit strange, but if we can work with any of the vendors that are pulling this in, I'd love to see the compatibility. This isn't quite ready yet, but I just wanted to put it out there, if anyone's open to that.
Will need help. I… the PR exists, it is old.
I will update in Slack and in the next meeting about the status, but just to get on the radar.
And that's it.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 28:00 Okay, yeah, I… do you happen to have the link to the PR, so I can put it here, or just take it from Slack?
**Jared Freeze (Embrace)** 28:08 No. I can add it here. I didn't want to add it, because I don't want people to think it's ready for review. Oh, okay.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 28:13 Okay, got it.
**Jared Freeze (Embrace)** 28:14 Yeah, it can't be published yet, but it… we're good now.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 28:21 Okay.
Really quick, I have been… so I've been talking to the, the Android folks… in the client's instrumentation SIG about starting a new… Temporary working group for working on sessions.
The idea would be to, work towards a spec, maybe an OTAP.
Where we would discuss, things like the data model, API, Maybe sampling, also representing sessions, you know, on… You know, as entities, and how that would affect… How that would affect the SDK, maybe… so, like, we're kind of expecting that the outcome of that, group would be an OTEP, and then some changes to the spec.
they've been talking about this for so long that, I think the, the… The, you know, the feeling and, you know, from… Was that, if you don't spin up, like, a dedicated group for this, you know, it may just drag on forever, so, I'm just, like.
sharing it with you, so if you… if you are interested in… in participating in that as well, that's probably something that's coming up soon. I'm planning to open an issue in a community to get this started sometime soon.
**Joaquín Díaz** 30:02 Could you share data on the… on our channel?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 30:06 Yes, yes, let's do this. I will share that.
Okay, so we're at time. Anything else really quick?
Must.
**Jared Freeze (Embrace)** 30:21 All good.
Thank you.
**Wolfgang Therrien** 30:24 Thanks, Bill.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 30:26 See you later, have a good week.
