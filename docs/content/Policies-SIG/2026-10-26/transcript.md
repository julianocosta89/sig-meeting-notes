SIG: Policies SIG
Date: 2026-10-26
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Jacob** 01:25 Pete.
I have a hard stop today, unfortunately, at the 30 mark.
**David Ashpole (Google LLC)** 01:35 That is… Okay.
But… I do as well.
**Jacob** 01:39 Cool.
Yeah, unfortunately, I'm bummed that, I'm bummed that, Jack can't join today.
**David Ashpole (Google LLC)** 02:08 Oh, yep.
**Jacob** 02:08 Because this would have been… useful. But even if it's, you know, just us talking about this, it's fine.
**David Ashpole (Google LLC)** 02:17 Well, that, that Jack. I thought he meant Jack Burke.
**Jacob** 02:21 Oh, no, not that far.
He was… I mean, I guess both Jacks were advocating for Glob.
**David Ashpole (Google LLC)** 02:30 I also think we should probably do Globe.
**Jacob** 02:34 You want to just get into it?
**David Ashpole (Google LLC)** 02:36 Yeah, let's get into it.
**Jacob** 02:38 So, I understand the argument, you know, against regex.
I guess… the issue around it is relating to, that, like, Go technically doesn't have a… is it Go that doesn't have, like, a default… like, a standard library RE2 implementation?
**David Ashpole (Google LLC)** 03:04 No, there's, like… 6 or 7 languages. Go has one. It's like…
**Jacob** 03:09 Yeah, I was like, I'm pretty sure they'll go help.
**David Ashpole (Google LLC)** 03:11 Java, Python… So let me see if I can find the list that I pulled together.
So it's 11 of the 13 OpenTelemetry SDK languages.
are not RE2.
So I think it's only Go and…
**Jacob** 03:41 That's, like, so shocking.
**David Ashpole (Google LLC)** 03:44 I… right.
I was surprised by it as well, because in Go, everything is… is RE2.
**Jacob** 04:03 Which patterns… work in regex, but not Glob.
Like, I'm trying to think about what we lose by doing this.
**David Ashpole (Google LLC)** 04:14 Yeah, yeah.
**Jacob** 04:15 It really just has, like, Wildcards, right?
**David Ashpole (Google LLC)** 04:20 Wildcard… it's a, star matches any number of characters, including none, and question mark matches any single character.
It's basically if you're looking for any particular pattern, right? So if you're like, oh, I want something to start with this, end with this, or include this in the name.
like, you can do that with… with Glob, right? So it's pretty similar to what you had with, like.
All of your starts with, end with.
Stop.
**Jacob** 04:46 Yeah.
But you don't get things like… You don't get, like, counts, ranges, or groups, right?
**David Ashpole (Google LLC)** 04:54 There's no extraction.
possibility where, like, oh, I want to take this thing out?
And there's no… or I guess this is just for matchers. But yeah, there's no, like, groups, right, in it.
And then…
**Jacob** 05:09 Yeah, the biggest thing would be, like, something like, I want, you know, I want to match, like, a credit card number, right?
**David Ashpole (Google LLC)** 05:16 Exactly, exactly. So, my… my proposal is that we remove… we do glob for everything except redaction.
And that redaction is its own policy type that has regex.
And then the SDKs wouldn't implement production.
**Jacob** 05:33 That's just so annoying. I think the problem is that, like, you know, when I'm thinking about, you know, the value of regex, it's the… I want to be able to see if I can… if I find a credit card number in a log, and filter that out, right?
And losing that feels like…
**David Ashpole (Google LLC)** 05:55 You'd want to filter out the whole log, or you would want to redact the credit card number out of the log?
Because my wife…
**Jacob** 06:02 socialism as well.
**David Ashpole (Google LLC)** 06:02 been that, like.
**Jacob** 06:03 either.
**David Ashpole (Google LLC)** 06:03 Okay.
**Jacob** 06:04 But in order to do that, I need to match where there is a credit card number.
**David Ashpole (Google LLC)** 06:10 Yeah, I… I definitely agree we need it for redaction.
**Jacob** 06:18 But it's not just… we need to be able to match on it, right?
**David Ashpole (Google LLC)** 06:24 For filters, and for.
**Jacob** 06:25 Except for the initial filter.
Because otherwise, you don't know what log group you're selecting.
**David Ashpole (Google LLC)** 06:37 Sorry, are you saying in order to be able to do a redaction, or are you saying, That you want to be able to drop.
Credit card logs entirely.
**Jacob** 06:49 I think that some users will want either, but even if it was just redacting credit card numbers. You wanna… it doesn't make sense to, like, scan through every log.
to do… that reduction.
Right, like, matching all to then say, okay, now run the secondary regex feels very…
**David Ashpole (Google LLC)** 07:18 No, so it would be that the… In my proposal, there would be a separate Policy.
for redaction.
So you would have… It wouldn't be part of the transform policy, or part of the filter policy.
And it would have.
**Jacob** 07:35 A different matcher.
**David Ashpole (Google LLC)** 07:36 than the other ones.
**Jacob** 07:37 Yeah, in my mind, redaction is part of transform.
Is that, like, redaction is a type of transformation.
But even so, it's like, I think that… having, like, losing the ability to match on regex is, like, a pretty big loss, I think.
Like, their… the ability to say.
Like, let me pull up some of the policies that I… To my company.
**David Ashpole (Google LLC)** 08:03 Yeah, that would be really excellent. I think…
**Jacob** 08:05 Yeah.
**David Ashpole (Google LLC)** 08:05 I think the question for this group is just gonna be… Right now, I've been hoping to treat policies as Mostly all-or-nothing support, where generally, like.
If you implement most of the fields in a policy, you implement all of them.
I think otherwise it becomes just a little bit harder to reason about.
**Jacob** 08:28 Yeah.
**David Ashpole (Google LLC)** 08:28 What policies are gonna work where?
we could go back on that, right, and have regex and glob, but have some things ignore policies that have regexes, right?
**Jacob** 08:37 Yeah.
Here's a good tip.
**David Ashpole (Google LLC)** 08:39 One direction.
Do you want to share?
**Jacob** 08:43 Yeah, I can share. This is… I mean, technically company… this is, like, sort of company internal, but it's… it's fine. It doesn't… it's okay that this… if somebody.
**David Ashpole (Google LLC)** 08:51 It's just recorded and posted to the public internet, so, you know.
**Jacob** 08:54 If somebody sees this, like, we have this in our product info, so it's, like, really not the end of the world. Actually, maybe I'll show the demo environment so that I'm not actually accidentally sharing something bad.
Yeah.
It's probably a better idea.
Ugh, but there's only, like, two policies in this. One second.
I'll go to, like, our actual demo environment, and we should have more there. Great.
Can you see the screen?
**David Ashpole (Google LLC)** 09:27 Yep.
**Jacob** 09:28 Great.
So let's just, like, click on this one, and just see what it looks like.
This one's pretty boring.
We have to find one that's, like, mildly interesting. Like…
**David Ashpole (Google LLC)** 09:44 Do you want to drop one, right? Or… Redact.
**Jacob** 09:47 No, I want one where the matcher is, like, mildly interesting.
**David Ashpole (Google LLC)** 09:56 Yeah, the conclusion I came to is, like, all the interesting matches are gonna be in redaction.
And so, like, pairing up regular production.
**Jacob** 10:05 Yeah.
**David Ashpole (Google LLC)** 10:07 It was, like, one way forward.
**Jacob** 10:09 These are all, like, really boring.
Let me just open…
**David Ashpole (Google LLC)** 10:13 You can also just, like, copy it and paste it into a doc and share the doc if…
**Jacob** 10:18 No, it's… I mean, I'm sure we can find… we'll be able to find one here. Just, like, this is our demo environment, where data is, like, pretty boring.
So usually, like, most of these are just, like… You know, matching on pretty boring stuff.
Like, the first one that I pulled in my, like, real environment was interesting, and of course, none of these are, because that's just how it works.
Here we go. This one's mildly interesting.
Not really. But, like, you can sort of see what I'm getting at, right? It's like… I want to look at the url.path, and if it starts with this, and the body… You know, also has this thing.
like, this would work, I think, in a glob, but imagine, you know, for example.
I wanted to match on anything that is feature live, and then long pull and short pull, but not, you know, medium pull, or something.
Like, you lose that ability with Glob.
**David Ashpole (Google LLC)** 11:15 Yep.
And this is… what kind is… this is a redact… yeah, this is a redact.
It's like, I totally… I definitely get the use case for redaction in particular, that it's, like, extremely necessary, and we can't really do redaction without some sort of… More… something more advanced than a glob.
**Jacob** 11:35 Yeah.
I might just go to my non-demo environment, just so I can show you one of these, because this is… these are all really boring.
I just feel like for… if we're gonna, like, go through some examples, we need some more interesting data.
**David Ashpole (Google LLC)** 12:02 I think the other… the other thought I had was, like.
If there's a way for us to… I… I'll put out a case, and then you can tell me whether it makes sense to you. I think that.
**Jacob** 12:13 signature.
**David Ashpole (Google LLC)** 12:14 we have.
**Jacob** 12:14 Yes or no?
**David Ashpole (Google LLC)** 12:15 Okay, here we go.
That is quite the regex.
**Jacob** 12:19 Yeah, great. I want something that starts with this.
but…
**David Ashpole (Google LLC)** 12:25 And then…
**Jacob** 12:26 you know, I'm doing, like, some back matching on it having something.
**David Ashpole (Google LLC)** 12:30 Right,
**Jacob** 12:32 And then, like, this one…
**David Ashpole (Google LLC)** 12:37 What kind was that? Sorry, that looked really interesting.
**Jacob** 12:39 This was just a sample one.
**David Ashpole (Google LLC)** 12:42 Okay, and then you're trying to… So you're trying to… oh, I see. You're trying to change the… Severity of those particular logs.
**Jacob** 12:55 Yeah.
**David Ashpole (Google LLC)** 12:55 That's very interesting.
**Jacob** 12:57 Like, you could imagine, this is actually a good use case where, I mean, you can read the description here.
It's like, let me… I'll actually go here, which will have it.
Bonsai Source… So, like, This one is, you know, we're matching here… why don't we show the description in here? We should really do that. Anyway.
Successful post, you know, requests are being logged 6.9 million times per week for Cloud Run. You know, these are, like, really low value, but they may be useful, so, like, you know, change them into debug, because they don't need to be info, right? Like, this to me feels like a pretty standard thing.
We could choose another one where it's, like.
Let's see… these are all, like, exact… I guess we're not doing a bunch of regexing right now.
Oh, like, this one is, like, another redact.
Or, like, it's some secret service.
**David Ashpole (Google LLC)** 14:05 The ad… the ad was really interesting to me.
**Jacob** 14:08 Yeah.
**David Ashpole (Google LLC)** 14:08 So what I was.
**Jacob** 14:09 That's what I was gonna say.
**David Ashpole (Google LLC)** 14:10 Over.
**Jacob** 14:11 You're good.
**David Ashpole (Google LLC)** 14:12 What I was gonna say is… I think we… I think we have to have Glob.
Or something similar for SDKs.
**Jacob** 14:26 Yo.
**David Ashpole (Google LLC)** 14:27 I don't think there's a path, really, for SDKs to have good RE2 support. Like, as a general.
**Jacob** 14:33 So…
**David Ashpole (Google LLC)** 14:34 Yeah.
**Jacob** 14:35 Can you maybe explain to me why… like… In my mind, what we could do… is have a… like, the way that I do this in, in Go today is make it so that you can select, like, a regex backend, so that you can decide which regex implementation you want to use.
Like, could we not do something similar here for SDKs? Where they could optionally provide a regex backend?
To then use for this matching?
**David Ashpole (Google LLC)** 15:11 I… so… Definitely they could, right? I think it's the question of… I think there's… It's like, if we only provided regex and not GLOB, or something Glob-like, I think the question is, would we get Would we end up with consistent support for policies across languages?
**Jacob** 15:39 Yeah.
**David Ashpole (Google LLC)** 15:40 For most users. And I think the answer is… Probably no.
Like, some languages might implement it.
But especially the long tail wouldn't, I don't think, implement, like, proper RE2 support. So, I feel like that eats into the kind of universality that we're going for here. I feel like.
**Jacob** 16:00 Yeah.
**David Ashpole (Google LLC)** 16:00 These are just kind of an important part of that.
No, I agree. Certainly.
**Jacob** 16:04 I agree.
**David Ashpole (Google LLC)** 16:05 I think that maybe the plugin, like, provide your own RE2 engine model could work for… if… if regexes were optional, right, so… you know, we have something, either Glob or something else, that is implementable.
by SDKs in a pretty straightforward way, and then, like.
maybe we… maybe some languages go, obviously, but, you know, the Javas and Pythons of the world that have pretty good contributor bases would implement regex support on top of that.
Or make it pluggable.
And then there would be some that only support Gob, right? But I think… My main point is just, I feel like we need something… something like Glob for SDKs, and then… And then I think we… Yeah, I think it's probably a must to have glob support, and then maybe we have Regx alongside it. That's kind of, like, where I'm at.
And.
**Jacob** 17:12 Yeah, I think that there's something there. We could maybe do some… I mean… This is, like, one of those things where it's very frustrating, to do.
Sorry.
Like, I would really like to avoid… needing… needing a way to do the same action in two different systems, right? Like, you can imagine a world where we have support for both, and somebody could specify one or the other, and then the implementation could choose.
And then if it can't run that, then it just doesn't run. But then it's like, your syntax gets a little strange, where it's like.
you know, You would specify a glob matcher or a regex matcher.
**David Ashpole (Google LLC)** 18:02 I think he would…
**Jacob** 18:03 avenue.
**David Ashpole (Google LLC)** 18:05 the way I would put this is, like.
Everything would be required to support GLOB.
And we would somehow mark regex as optional. So, if you write a policy with a regex.
you're opting into a more limited set of implementations.
**Jacob** 18:22 Yeah.
**David Ashpole (Google LLC)** 18:23 If you can't express a policy as a glob, you would do that.
And then, only when you need the power of regex would you… something like that, where, like, there's one that… there's, like, a precedence order, it's not, like, an ambiguous, like, oh, like, do whatever you feel like, you know, if you like writing RE2, write RE2, right? Like…
**Jacob** 18:44 I also think that, like, the… at least in the met… in the… API syntax… the API spec that I wrote, I think that you could do something where you could still transmit the policies that have the regex, and then for the back… for the implementations that don't support it, it would just return an error for those policies, and it would be, like, a fail-open error, where it's like, oh, you sent me a policy that, like, I can't Run the entirety of, right?
I mean, like…
**David Ashpole (Google LLC)** 19:13 The metrics we produce say, like, hey, you know.
X number of policies I don't support, right?
**Jacob** 19:20 We don't surface that.
**David Ashpole (Google LLC)** 19:22 this way.
**Jacob** 19:23 Yeah, I have… I have support for that right now in the API that I wrote, where it's like, you can do… I mean, I'm sure there's a more correct way of doing this, and I'd like for us to do it the right way, but eventually, I'd like it to be sort of that syntax highlighting-esque, like.
Underline, you know, this part… this, implementation failed to run.
On this part of it.
Great.
sort of that, invariant check, I think would be good. I guess I'm still just so… Shocked that, like.
Languages don't have… like, wait, so what does it look like in Java? Java just doesn't have an RE2 library?
**David Ashpole (Google LLC)** 20:04 So they have… I think some of them have one, but it's implemented in a way that's problematic.
Where they have… What's it called?
It's like backtracking or something.
**Jacob** 20:21 So, like, Google has a RE2 library for Java.
But… like… I just don't understand how a language can't have regex support. Like, Perl has, like, has regex support, you know what I mean? Like… Yeah, Isha hand raised?
Nope.
**Isha Bhardwaj (Individual Contribution)** 20:46 Yeah, so… In the last meet, like, I wanted to have this discussion, like, last time, like, Jack said that the policy assumes a late sampling decision, while the SDK decides a span start. So, like, David asked, like, what that actually means in practice. So, what I checked, I took every trace measure in the draft, and then compared it with, what an SDK sampler actually receives.
And I ran a probe on the Python SDK and checked the Java signature. So what I found, like, most of the mature targets can't be evaluated at the span start. Like, the span ID, status, events.
scope and the later added attributes. So, the practical risk, like, what I find is that the matchers are in AND. So, like, if an SDK ignores a matcher, it can't evaluate the policy matcher more than intended. So a drop policy could, like, discard the spans the author wanted to keep. So an SDK should skip the whole policy.
So, like, I also put the table and the probe in a comment on the PR.
And just share…
**David Ashpole (Google LLC)** 21:56 I saw that. I'd like to finish up the discussion that we're having on the globs before we move on to sampling, if that's okay.
**Isha Bhardwaj (Individual Contribution)** 22:03 I'm so sorry, it was like Jacob said, like, oh, pretty much tight on time, that's why.
**David Ashpole (Google LLC)** 22:08 Okay.
Jacob, so my proposal, just so that we can move forward… I still think we should at least consider switching to Glob and adding regex support later. I do agree, though, I'll take an action item to dig into why they don't support Regx, or why they don't like it. I had looked at it two weeks ago, and I've forgotten.
**Jacob** 22:34 Yeah.
**David Ashpole (Google LLC)** 22:34 I kind of… Like, the fact that declarative config went this direction makes me, like, somewhat inclined to at least align with it initially.
Like, that's kind of my default bias, but… I think we should think a little bit more, like, generally about how we How we want to handle fields that we kind of want, but that we know that this kind of 70-80% of implementations might not be able to implement, right? Like, the fields for… Advanced, more capable, whatever, engines out there.
**Jacob** 23:10 Yeah, I… I agree. I think that, like… Before we do this, I mean, I think that we should just have, in the matcher syntax, the ability to specify glob and specify regex, and then they can live… they can coexist. And I think that that's an easy enough solution, where it doesn't really, like, break either… It doesn't break what I'm doing today, it doesn't break the SDKs.
**David Ashpole (Google LLC)** 23:36 Okay.
**Jacob** 23:36 So I think…
**David Ashpole (Google LLC)** 23:37 I was…
**Jacob** 23:37 Sorry.
**David Ashpole (Google LLC)** 23:38 Okay.
I think we can do that. I think we need to… I think we just need to make sure that in the spec, we talk about what happens if you have partial support for a policy, like, what your behavior is, because you need to implement the parts you can implement and treat the parts you can't Some sort of, like, Non-error?
But not implement… like, there's a new state that we have to introduce, sort of, that's sort of…
**Jacob** 24:05 God.
**David Ashpole (Google LLC)** 24:06 Yeah, you know.
**Jacob** 24:07 I had called it a, fail-open compile error on a per-policy basis.
**David Ashpole (Google LLC)** 24:14 Okay.
**Jacob** 24:14 So, like, in the implementations, I was considering… the building of… like, once I received the policies, I considered the building of… I was doing this in this, like, database approach.
Where you compile the policies that you get into these databases, these matcher databases.
And so I think in this case, it would be I failed To compile this policy into the database.
I think that's…
**David Ashpole (Google LLC)** 24:41 I think that's reasonable.
Now let's move on to the… so we'll plan to do both.
I think that answers the second question for sampling as well, which is, for sampling, we have… One set of fields that can be… Implemented by a head sampler and a tail sampler, and another set that we know can only be implemented at tail sampling.
Yeah. The only… so we could apply the same solution here and say we'll have both, we'll have rules for how you handle fields that you can't Recognize in the policy engine.
implementation. I think my biggest hesitation for sampler policy is that I had hoped that we could follow the consistent probability sampler spec.
Which means actually mutating the… the context.
Or, sorry.
**Jacob** 25:33 Yup.
**David Ashpole (Google LLC)** 25:34 The, the trace… trace state.
**Jacob** 25:36 Yeah, the illustration.
**David Ashpole (Google LLC)** 25:37 to record it. So… Now we have, kind of, not just, like.
a restricted implementation and a more expansive implementation, but we have two modes where you're saying, yes, propagate trace state things, versus tail sampling obviously can't do that. So… I… to move forward, I would actually be more inclined to trim it down to what's supported by head sampling, and to punt On how we want to do this.
But my only hesitation there is that if we lock ourselves into saying that we are going to Follow consistent probability sampler, trace state setting stuff, then obviously we… this just becomes a head sampler policy, and we should probably just name it as such.
**Jacob** 26:24 I think that's acceptable. I mean, I think that, To me, well, you can do… I thought, consistent… the consistent probability sampler in the collector Propagates TraceState, no?
**David Ashpole (Google LLC)** 26:38 It.
It's… I mean, it can't propagate it through trace context. Like, it may set it, or it may use it.
**Jacob** 26:48 I thought it was setting the trace thing, let me check.
**David Ashpole (Google LLC)** 26:52 Like, it… TraceState is something that… gets sent on the wire with the request, right? So by the time it gets to the collector as data.
You can maybe modify it for posterity, so that if you generate metrics from it, it's correct.
But I don't think you can send it to anyone downstream.
Maybe that's not important.
**Jacob** 27:14 I thought you were…
**David Ashpole (Google LLC)** 27:15 You're right.
**Jacob** 27:15 Thanks.
And all modes, information about it is added. Yeah, no, it is added. Here, look at this.
**David Ashpole (Google LLC)** 27:24 Okay.
**Jacob** 27:25 Because I remember reading this as, like, Josh was writing it.
And so… and this is what I was… I was going off of for what I was doing initially.
**David Ashpole (Google LLC)** 27:39 Didn't… we didn't take notes.
Alright, you can keep talking, I'm just taking, taking notes.
**Jacob** 28:20 Oh, okay. Yeah, I'm pretty sure it is added into the, like… the… I think we do, in the collector, write the trace date on the trace context.
Which is… On the headers.
**David Ashpole (Google LLC)** 28:44 So…
**Jacob** 28:45 of that request.
**David Ashpole (Google LLC)** 28:46 So the span itself… Did this span have trace state? I don't think so.
**Jacob** 28:52 Well, the span has never emitted, solo, right? Like, it's in the trace envelope, is it not?
No, no, it is. It is admitted.
**David Ashpole (Google LLC)** 29:04 That is… that's what I saw.
Disjointed data by the time they get to the collector.
And the collector's applying a stateless transformation to them.
**Jacob** 29:14 Yeah, I think you are encoding it on the spam message.
**David Ashpole (Google LLC)** 29:20 Right, you're encoding it on the span, but not in headers that get propagated from the application that recorded it to the next application down the chain, right?
**Jacob** 29:29 I have to… let me look at the,
**David Ashpole (Google LLC)** 29:32 I think this is an action item we should take.
Isha, is there anything you want to add?
**Isha Bhardwaj (Individual Contribution)** 29:39 Yeah, so, like, I also suggested, like, two approaches. I want to go ahead with the approach second, like, one policy type with the head, like, as you said, the head evaluating map role matchup.
The rule is that if the SDK cannot fully evaluate a policy, it skips that entire policy rather than silently ignoring the unsupported matchup.
Because the advantage here is that the one shared policy structure with explicit information about each matcher's head, sampling compatibility. The major drawback that I think is that implementations need to respect the And skip the rule consistently. And the policy format must also be clear, to define, like, how those markers, like, works.
If that makes sense.
**David Ashpole (Google LLC)** 30:36 Yep, yep. So this is the same thing we just talked about, where we want to support tail sampling matches as optional, and define, how that behavior is handled.
optional.
**Jacob** 30:46 I do have a hard stop, so I do have to head out.
**David Ashpole (Google LLC)** 30:49 Okay, all right, so we got through two of the three, we have some action items.
Yeah. I can work on both of those and send stuff for them.
**Jacob** 30:58 Cool. And yeah, we can continue, we can chat in the channel about option, 3. Are you gonna be at KubeCon this year?
**David Ashpole (Google LLC)** 31:05 Yeah.
**Jacob** 31:06 I just got…
**David Ashpole (Google LLC)** 31:07 Bunch of progress, huh.
**Jacob** 31:08 Added, so let's… let's, like, maybe just have a couple syncs while we're there, and just get a bunch of these, a bunch of this stuff up.
**David Ashpole (Google LLC)** 31:14 We can sign up for a SIG slot, I think, at the…
**Jacob** 31:17 Great idea, sir, great idea.
**David Ashpole (Google LLC)** 31:18 observatorium.
Bing, if that's still exist.
**Isha Bhardwaj (Individual Contribution)** 31:21 Just a small part. I also performed a few texts for your conference repo. Is it okay to, like, share that with you, Jacob, to just check it?
Sorry? On the sec?
I have added the text… You have shared the report, the previous, meet, so I've added a few tests into that. I'll just share the… on the Slack, if you're inclinable, just check them.
**Jacob** 31:46 Yeah, yeah, I'd love to see it. Let me know.
Okay, I gotta go. I gotta go, unfortunately. But thanks, everyone.
**David Ashpole (Google LLC)** 31:52 Yep, see ya.
**Isha Bhardwaj (Individual Contribution)** 31:54 Bye.
