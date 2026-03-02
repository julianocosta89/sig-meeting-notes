SIG: Specification SIG
Date: 2025-08-26
Duration: 37 minutes
============================================================

## Zoom Recording Transcript

**Tigran Najaryan** 02:34 Everyone.
If you have a topic to discuss, please add to the agenda. We'll start in a minute.
**GZ Gregor Zeitlinger** 02:54 Hello?
**Tigran Najaryan** 02:59 I agree, Kirk
Okay.
Let's start. Trask, I think. Is Trask here? Yes, Trask, you have the first item there.
**Trask Stalnaker** 03:29 Yeah, Carlos had, requested that
I bring this to the spec meeting one last time before it is merged.
… So, I'm here. video's not working for some reason.
… But, … oh, there we go.
I think it's ready to be merged. I think the only thing, possibly is,
Kayla has a PR also to the spec matrix.
So… there is… …
So, Mark mentioned that there would not be a merge conflict. That is true, but it will prevent
the merge conflict from being merged, that conflict from being merged, because of the workflow. There is an automated workflow in this PR that will fail if the matrix markdown doesn't match the YAML
So anyway, I guess, just need a decision from the maintainers of this repo which one to merge first, and then Kayla or I can fix up.
the other one.
**Josh Suereth** 04:47 I took a look at this, I didn't make a comment, but if we have the option to express preference, I'd rather have your PR go in first, because it makes reviewing Kayla's PR way easier for us, because we can look at only the Ruby-related checks, and verify them.
So, that would be my personal preference, if we have an option. I don't know how the other maintainers feel.
**Kayla Reopelle** 05:16 I'll chime in. I'm completely fine either way. I am happy to be, like, the first guinea pig on this spec compliance PR and see what it's like as a user to update it, so if that feedback would be beneficial, happy to take that approach.
**Josh Suereth** 05:35 We could also gate this on your feedback. If you're like, hey, this is really annoying, you could actually make a comment on Trask's PR of, like, hey.
Maybe we should think about this more before we merge it, yeah.
**Kayla Reopelle** 05:48 Yeah, that works too. I could pull it down and try to update it.
**Tigran Najaryan** 05:57 So, what do you want to do, Trust? Wait for… for that?
**Trask Stalnaker** 06:00 Yeah, Kayla, why don't you, …
do that, and then just post your feedback, on this PR, and, once your feedback
If it's, if everything looks good, then, maintainers can go ahead and merge this one. Otherwise, I will address any feedback on the PR.
**Kayla Reopelle** 06:22 Awesome, sounds good.
**Trask Stalnaker** 06:24 Thank y'all.
**Tigran Najaryan** 06:25 And once that's done, we're ready to merge, we have enough approvals.
Okay.
**Kayla Reopelle** 06:34 I did add a question on my PR yesterday, that is somewhat related. Do you need an approval from another Ruby maintainer before you can merge in spec changes, or spec compliance matrix changes?
**Josh Suereth** 06:50 So, so generally, at least on my part, I usually try to go verify in some fashion, and….
**Kayla Reopelle** 06:56 kind of….
**Josh Suereth** 06:57 Trust the maintainers. So, like.
coming from a maintainer, we trust that you know what you're talking about, but I, … depending on which one it is, I like to go just check docs and things myself, which is why I never finished reviewing yours, because I think I only verified, like, two of the checks. That's all, yeah. Okay.
**Kayla Reopelle** 07:16 Yeah, we haven't made a lot of docs updates, so the changes would be probably found largely in pull requests in our right bill. But if it's important to have docs changes, I can work on those too.
**Josh Suereth** 07:29 I think the question would be, the features that you added, if users don't know how to use them.
That's… that would be the problem. So if it's not in Docs or in, like, RubyDoc.
I'd be concerned, but if you think, like, it's discoverable via Ruby Docker looking through the API, you're fine.
**Kayla Reopelle** 07:48 Okay.
**Josh Suereth** 07:49 Don't want to make this onerous, but it's….
**Kayla Reopelle** 07:51 You're right.
**Josh Suereth** 07:52 Yeah, if that makes sense.
**Kayla Reopelle** 07:53 Yeah, that makes sense. No, I think we're covered then, because the things are documented very clearly in RubyDoc, we just haven't moved stuff over to OTEL.
And we do have users who are using the features, so it's been at least discoverable by some people.
**Josh Suereth** 08:09 Yeah, and when I said documentation, I didn't even think about OTel Docs. That's how bad.
**Kayla Reopelle** 08:13 Oh, I see, okay.
**Josh Suereth** 08:15 Only thought about your method docs.
**Kayla Reopelle** 08:17 Got it! Okay, that makes more sense, yeah. Good to know.
**Tigran Najaryan** 08:26 Okay.
Next is Trasko Robert.
**Trask Stalnaker** 08:31 Yeah, it's, Robert's PR here at Toproto as part of the, in the LogSig. We want to make a blog post about, the upcoming changes to complex attributes.
And we wanted to gate that blog post sort of on the first PR that, Robert sent, which is now merged.
But then we want to point people to this…
PR ad in the blog post as, like, here's where it is actually changing now in the next version. And so, it would be great if we could have a proto-release
…
Soon-ish, and then we can mark this one as ready to review and reference it in the blog post.
Does that make sense?
**Tigran Najaryan** 09:35 Yep.
**Robert Pająk** 09:37 I think there was one, PR related to profiling, which may be required to double-check.
Something related to simplification? Yeah, this one.
So maybe just double-check if it's worth shipping this one.
**Tigran Najaryan** 09:51 Do we wait for this before the release? Is that what you're saying?
**Robert Pająk** 09:55 Yes, yes, yes, because I think it can be… it may be handy for the profiling sick.
**Tigran Najaryan** 10:03 Anyone from profiling here? No, I don't see anyone.
**Trask Stalnaker** 10:09 I can ping them in Slack.
**Josh Suereth** 10:12 Yeah, if I remember right, I do think they… they did want to get this in, if I recall correctly.
Man, it was only Thursday was the meeting, and I remember we discussed it, and I can't remember details. Can you scroll up a sec to see what the latest comment was?
This is about stack table.
Yeah, as long as Alexi's comments are, fixed, I think this one is probably good to merge. So, we should follow up with them, but….
**Tigran Najaryan** 10:41 I mean, we can't merge, there's a merge conflict as well.
**Josh Suereth** 10:45 Okay.
Yeah, maybe follow up with them and see what they want. Let's do that.
**Tigran Najaryan** 10:52 Yeah.
Okay, I commented here, let's see, if they don't respond, we can go ask in Slack as well.
Trustee, you were saying something?
**Trask Stalnaker** 11:02 Thank you.
No, no, that's a great… that's great. Appreciate it.
**Robert Pająk** 11:07 part for me, because it was a 5-minute, you know, time box, I just want to share that you can also review and include the draft PRs. I made, yeah, I also made… Yeah, and I also created the really expect PR, if you… the first hyperlink in the description.
Which is also how…
the end goal may look like, so it's not something that we will just, you know, make… it will need to be, like, … there'll need to be separate steps, so here, I'm not making things in development, this is how it could look after things are, you know.
Going through the development stage, and then getting stable at some point of time.
And so, yeah, so this is kind of the end goal, how I can… how it could look like if we have it, you know, just finished.
**Tigran Najaryan** 12:03 Okay.
**Robert Pająk** 12:06 Thank you.
**Tigran Najaryan** 12:07 Thanks, Robert.
So let's wait for the profiling sick to respond, and we'll decide whether we release 1.8 now, or we wait a bit for them.
And yeah, for them to go. Sounds good.
Okay, Gregor, you're here, right? You were here, yes, you're here.
**GZ Gregor Zeitlinger** 12:32 I am.
Yeah, last week, I… explained what I want to do with an authenticator.
Now I came up with a… POC implementation, and Java.
And now I want to know how to proceed, …
Should we discuss here what I have implemented, or should I create a specification PR and then discuss there?
**Tigran Najaryan** 13:07 So there's… there's an issue….
**GZ Gregor Zeitlinger** 13:10 How it works.
**Tigran Najaryan** 13:12 you want to present now, I can stop sharing if you want to show something.
**GZ Gregor Zeitlinger** 13:18 Yeah, let me do that.
Can you see?
My IDE?
**Tigran Najaryan** 13:40 Yep.
**GZ Gregor Zeitlinger** 13:42 Okay, court.
So, basically, it's this. So, I added a new interface authenticator.
Export Authenticator, and this corresponds to a component in the declarative configuration, bingo.
And I kept it minimalistic, because this is the thing that fulfills the use case I have.
And, …
I want to… yeah, I want to get feedback if this is, enough, or if there are other use cases
That have been discussed in the past that I should think about before We put it into words.
**Tigran Najaryan** 14:27 So this works with basic auth only, right? If you want to do anything more complicated.
I guess this wouldn't work, right? Anything that requires workflow, essentially.
**GZ Gregor Zeitlinger** 14:40 No.
**Tigran Najaryan** 14:41 Yes, it does.
It does.
**GZ Gregor Zeitlinger** 14:44 Yes, it does. I designed it for the GCP authenticator, but,
there's no, specifics about GCP. So, whenever,
request is created, this method is called, so you can have rotating tokens. This is the capability that was
Missing before, but maybe you mean something else.
**Tigran Najaryan** 15:08 I guess, so you're saying the flow would be executed by this method? This is not intended to just return some static tokens and headers, and that's it, right? It can just do the whole flow and return the token as a result of that.
That's what you're saying.
**GZ Gregor Zeitlinger** 15:23 So when you send a request, this method is called, and it can… it can, yeah, it can fetch a token.
**Tigran Najaryan** 15:30 It can do whatever it needs to do, yeah, yeah, yeah, okay, makes sense. Have you looked at, looked at what the collector authenticator's interface looks like? Is it similar to this, or different?
**GZ Gregor Zeitlinger** 15:43 No, I have not.
**Tigran Najaryan** 15:45 There is a… it may make sense to look at that, because it's sort of a prior art, and it serves a very similar purpose. There is an authenticator interface in the collector. You can implement an extension
That implements any sort of an authentication mechanism.
And it's used precisely for that same purpose that you have here, to plug in the… whatever auth you want to have in your exporter.
So maybe take a look at that, and if there's anything you can borrow as an idea from there, it could be probably useful to also have a consistency.
Between the collector and the.
**GZ Gregor Zeitlinger** 16:23 Authenticator?
**Tigran Najaryan** 16:26 Yes, Josh posted the link there.
**GZ Gregor Zeitlinger** 16:29 Okay, cool, thanks.
**Trask Stalnaker** 16:33 And also look at Robert's link, it's some prior art. It was, the AWS folks wanted something like this for supporting, the SIGv4 authentication scheme.
Which is more complex, because it also needs the request body.
But it would be good to… whatever, you design here, doesn't need to address that use case, but should be forward compatible with that use case so that they could build on top of your authentic… basic authenticator.
**GZ Gregor Zeitlinger** 17:12 Right, where is the link from Robert?
**Carlos Alberto Cortez** 17:16 In the chat.
**Tigran Najaryan** 17:17 Zoom chat.
**GZ Gregor Zeitlinger** 17:19 Zoom chat, okay, got it, thanks.
**Carlos Alberto Cortez** 17:21 Actually, probably we should copy that and put that in the docs, you know, so it's not lost.
**GZ Gregor Zeitlinger** 17:26 I think that right now, Okay, thanks.
**Tigran Najaryan** 17:45 Okay.
Ludmila, I think you have the next one.
**Liudmila Molkova** 17:50 Yeah.
So, I'm glad that Gregor is here as well. So, Gregor, this is about the pull request, you have for semantic conventions to add configuration,
So, the long story short, it's not, clear where the instrumentation declarative config should live.
One option has semantic conventions.
For example, there, we would define, some configuration for instrumentation, like, for example, HTTP headers that are opt-in, and at the same time, we would define,
Configuration option that controls this behavior.
It makes sense there. It's the single source of guidance for instrumentation authors. It's also something that eventually we hope to be able to generate. The actual code that would go and check with the declarative config, if the option is enabled, and then
Around a specific branch of the instrumentation code.
So far, so good. … the… then…
there is a question if we keep at least some of this in the semantic conventions, and the semantic conventions is the authority that, invents configuration options.
Then, should we also keep it in the configuration repository?
And if yes, then it reduces all sorts of problems. It will be out of sync, there will be problems with, getting it reviewed. For example, Greg, Gregor brought up the peer configuration.
And you know what? I'm… I left a comment, why is it the instrumentation configuration at all? It will keep happening as long as we keep these things in two different places.
…
So, I wanted to discuss with configuration folks, if they're present, any other folks here, what do we think? My proposal would be to figure out the story on how instrumentation
Part beliefs in the semantic conventions.
And we would figure out the tooling, or some other means to solve the rest of the problems.
Yeah, and here is how it looks now in the configuration.
**GZ Gregor Zeitlinger** 20:25 There's also a schema for that, and so this document is an instance of a JSON schema.
That is also in the configuration repository.
**Liudmila Molkova** 20:39 What we can do in theory, that, if…
we define configuration options inside semantic conventions. We could create, … … Document that describes this section.
And it follows…
the configuration schema. But my well guess is that under instrumentation development, any schema, any valid schema would be
Accepted, because why would there be any… limitations.
**GZ Gregor Zeitlinger** 21:16 Well, right now, the general part of instrumentation is regulated.
But, the language-specific ones is freeform.
The rationale is that…
The rationale is that for general, we should have some agreement on how this looks like, so that you can easily copy the general part
Between languages and not have a different behavior.
**Liudmila Molkova** 21:48 And this general part could still live in semantic conventions, or be, automatically brought up here if… if we…
Have energy to write this tooling.
**GZ Gregor Zeitlinger** 22:03 Correct.
**Tigran Najaryan** 22:08 So, I guess you're saying tooling to extract from here…
Into… into this file, essentially, instead of having it. So make one the source of truth and the other generated from that.
**Liudmila Molkova** 22:20 Yes.
Some form of this.
**GZ Gregor Zeitlinger** 22:27 Would this also apply to the part above instrumentation? So where you define how exporters look like?
**Liudmila Molkova** 22:35 No, only what affects instrumentation. So, for example, even the thing about the peer mapping.
I would not put it in the instrumentation, because I think it's the processor which should do it, but that's something we should discuss separately.
Right. But essentially, anything, only the things under instrumentation, development, and maybe general, because…
That's what we define in semantic conventions.
**GZ Gregor Zeitlinger** 23:10 Yeah, makes sense.
**Trask Stalnaker** 23:14 Tyler, I was sorry to…
I think you're the only person from Configuration SIG I see here, so was just one of… was just curious if you all had discussed this.
Previously, would this be good to, … the config sig con… is at the same time as semantic convention sig.
Maybe we could recruit… you all to come over to Symantec Convention SIG.
Next week, to discuss….
**Tyler Yahn** 23:50 Yeah, … Is the semantic adventures, like, every week?
**Trask Stalnaker** 23:55 Yeah.
**Tyler Yahn** 23:57 I think we just missed our… a chance then. …
Yeah, the configuration SIG is every 2 weeks, and so we'll… we would be meeting next week, but not this week, is the thing.
Yeah, I mean, I think it's worth discussing it. Like, I think that's… it's a good idea.
**Trask Stalnaker** 24:18 Do you know if there was any prior…
Like, the recollection that I had, and I think Lydmilla had also from previous discussions with Jack.
Was that, at that point, we were thinking that that, …
you wanted us to document it, define it in SEMCOM, and then you would land it in the schema here.
But sort of what we discussed yesterday in SEMCOM, and…
we were concerned about having it sort of… that two-step process seemed to make things more difficult, and so kind of the… we were leaning towards the idea of, does it make sense to just have it completely defined in SEMCOM and not…
Have the, sort of, Schema duplicated in both places.
**Tyler Yahn** 25:16 Yeah, my only concern, though, is that the config is going to have, like, … some….
**GZ Gregor Zeitlinger** 25:22 Guidelines around how it wants to be structured and what to use and what not to use within, like, that….
**Tyler Yahn** 25:27 ecosystem.
And so I think you'd want oversight into the development of the config itself.
Instead of it just being defined outside of it.
But
like, it's also, like, this instrumentation stuff is pretty, freeform, so I don't know if it's, like.
the end of the world. It's just, like, maybe there's a better way to also, like, pop… like, publish, like, our recommendations for how to develop?
configuration, because the semantic conventions I think we want to do right. But the idea is that eventually, like, third parties are able to also provide this kind of configuration.
So, …
Yeah, I mean, I think setting a good example of semantic ventures makes sense, but also, like, we want to, I think, make it accessible to everyone else that's going to write this to try to do things in a way that would conform and, you know.
In our style guide, essentially.
**Tigran Najaryan** 26:26 Josh?
**Josh Suereth** 26:27 Yeah, I think we should define what success looks like here, so we know if the trade-offs are working. We talked about this a bit in the SEMConf meeting, but, like.
One of the general concerns is if…
When I define semantic conventions for instrumentation.
I define the config somewhere else, and they fall out of sync with each other and die. That's problematic. I think, Tyler, to your point, like, this has to be an open extension point, so if someone defines their own
instrumentation, conventions, and things, they need to be able to do so without having to be in one central place for everything.
And we want to be able to, like, verify the config, right? So I think we have a set of values that we have to…
look at to evaluate where this goes and how to do it. My thing that I really want to emphasize for us is to put a strict
Interface of some fashion.
Where, like, the… the…
Configuration component, if you will, has a strict interface for how someone defines configuration for instrumentation.
And then semantic convention leverages that in… that when they define
Configuration and semantic conventions about a particular area.
But it… if you're opening up for 3P, that's even better, because that means it's a very strict interface, and it's very clear where the boundaries are.
But I think what we want to avoid is a failure scenario where I want configuration.
I want instrumentation, and I have to touch 12 different places across OpenTelemetry to make that happen, right? We want to get to a point where I'm defining, here are the signals I want, here's the configuration for those signals, and then I do some code gen and do things in various languages, right? We want to keep that as simple as possible.
Or have a central authority for, like, a particular area.
But this is where I think,
we need to define that interface. We need, like…
in semantic conventions, here's how I define an area. In configuration, here's how I define that area, and then we give those capabilities to people to say, here's how HTTP will work, right?
So, I don't know if you already have that in config, but that's kind of the thing I want to make sure we're building out if we, you know, as we move forward.
**Tyler Yahn** 28:38 Yeah, that does exist. And the validation as well.
**Josh Suereth** 28:44 Yeah, so it's not centralized, is what you're saying?
**Tyler Yahn** 28:48 No, it… no, and it wasn't meant to be, … like, it was always meant to be composable, especially for, like, third-party instrumentation, is kind of the key.
It's just, we're…
I guess there are, like, some conventions around, like, how we want to structure, the actual file format, I guess is all I'm saying. And so, like, we'd want to make sure that those, like, map to something here. Like, obviously, like, you can always, you know, fan things out or go really deep in configuration. How do you want to structure that? Like, there's different types within, the YAML specification that we want to, like, try to avoid or try to support. It's kind of those… those are the more of the things that…
I'm talking about.
**GZ Gregor Zeitlinger** 29:28 So I think, the extension mechanism is, provided by having a free form in the language-specific part. For example, under Java, the schema does not,
specify what you, should put there, and every, distribution, every SIG can put there, whatever makes most sense for them.
We're talking here specifically about a very small part, which is the general section that deserves more regulation than the rest.
**Liudmila Molkova** 30:04 It's small now?
But I envision it growing.
Especially if I had to link around this. So, how it might work, I guess, Tyler…
you probably have some design considerations on how things should be done in a free form, and JSON schema to validate them.
We can, …
absorb them in semantic conventions for this, if we end up doing, configuration in semantic conventions. And then, we would use these best practices,
And we would probably tag you folks on the PRs initially, And we could develop, …
Once we're happy with the outcome.
We could figure out the tooling to bring it to the configuration.
And this, exercise with semantic conventions could
Be the basis for developing the same for the third party?
Does it make sense?
**GZ Gregor Zeitlinger** 31:18 So you're saying we moved the entire schema to the semantic convention repository, right?
**Liudmila Molkova** 31:25 Under the general.
**GZ Gregor Zeitlinger** 31:29 I mean, yeah, no, what I'm asking is, this general section is, it's only part of the JSON schema. The JSON schema also covers the SDK-specific part. Do you also want to move that to the semantic convention repository?
**Liudmila Molkova** 31:45 No, only the instrumentation in general.
**GZ Gregor Zeitlinger** 31:51 Okay, so then the configuration repository would pull in this particular piece, and then compose the entire schema out of it. Yeah?
I think that would work.
**Liudmila Molkova** 32:09 This needs quite a bit of work.
…
Are we ready to do this work? I think we are still lucky in the vision and semantic conventions on how we approach configuration, and it sounds like a relatively big
project.
**Trask Stalnaker** 32:26 I also think we still need a green consensus from the configuration SIG.
**Liudmila Molkova** 32:32 Right.
**Tyler Yahn** 32:35 Yeah, I think we still need to take a look at this in the configuration sig, but I also…
I'm… I'm hopeful?
like, I think that bringing this, I think, over towards the semantic conventions is gonna better shape things, here.
But, yeah, I still, especially, like.
The mapping of this general to, like, the specific of the instrumentation, like.
I think that that needed more input, or it needs more input from, like, how instrumentation is going to get used, so that's, I think, going to be very helpful, but I think it also, like, needs to be structured in a way that's going to be helpful for downstream to, like, parse this as well. So, yeah, I'd have to take a look at this. I think there's missing…
recommendations here, is what I'm thinking, is all.
**Liudmila Molkova** 33:23 Okay, so then let's keep discussing it. I don't see this decision as a strong blocker to what Guragara is doing, though.
Saying that this configuration option is used to control Something in semantic conventions makes sense.
Regardless.
**GZ Gregor Zeitlinger** 33:45 So you mean we could use this as a first step?
the support request.
**Liudmila Molkova** 33:51 Yeah, I still keep my comments around the peer mapping, but yeah, like, as the approach that we document configuration options in semantic conventions, as well as configuration.
As a first step makes sense to me.
**Tigran Najaryan** 34:05 But there's still a risk of what you were saying, right, Ludmila, that this will diverge from what you have here.
The risk is already there. Once you merge this PR,
you'll… you'll end up in that situation when… so I was wondering if you want to maybe delay this a bit?
to wait for that discussion to happen between the SAM call and configSIG.
You guys want to do a follow-up discussion, right?
And make a decision, maybe?
And wait for that before merging this PR.
Up to you, just… just wondering if… what you want to do there.
**Liudmila Molkova** 34:41 So my reasoning is the follows. The only thing I want Gregor to add is the HTTP headers enablement.
And it's been out there for quite a while, and we have environment variables for this, and it's a relatively small thing that I feel
is okay if… even if it diverges, which is unlikely, that it will be contained. We can use it as an example, and we can see how it works. And there will be a precedent of using configuration and semantic conventions that will force us to figure out how to do things.
But there are other maintainers, semantic conventions maintainers here, and I'm curious what they think.
**GZ Gregor Zeitlinger** 35:25 I think it's fine as a step….
**Trask Stalnaker** 35:27 In the direction, …
I think we all agree that it's not the end result, and even a second step, potentially, Gregor, beyond this, that we could do in parallel with,
getting consensus with ConfigSig.
Would be to… propose a YAML
structure in semantic conventions in Weaver.
For documenting these… …
configuration options, because really we want it in YAML, not in freeform notes like this.
**GZ Gregor Zeitlinger** 36:10 Yep, I was expecting that, too.
**Trask Stalnaker** 36:14 Yeah, yeah, so that would be… I mean, it would be awesome if you…
can start kind of poking around and propose something, around the YAML structure also.
But I'm okay with kind of doing a few of these things in parallel. I don't think adding… I think adding it in the notes in freeform is okay for now.
**GZ Gregor Zeitlinger** 36:37 Yeah, I'm happy to also do that, if you give me, like, a hint what a good starting point is, what a similar document is that I can use.
**Trask Stalnaker** 36:48 You wanna chat in, …
declarative config sig on, declarative… the Java declarative… we have a Java declarative config meeting on Thursday, because Greg has been doing so much declarative config work, we split that off.
**Liudmila Molkova** 37:05 I can join your call.
**Trask Stalnaker** 37:07 Awesome, it's at 8 Pacific.
**Liudmila Molkova** 37:10 8 Pacific, okay. Awesome, thank you.
**Trask Stalnaker** 37:12 Awesome.
Take care.
**Liudmila Molkova** 37:17 Wonderful, thanks a lot, everyone.
**Tigran Najaryan** 37:22 Okay, that's all we had in the agenda. Any other topics, anyone?
Okay.
Thanks, everyone.
**Trask Stalnaker** 37:49 Bye.
**GZ Gregor Zeitlinger** 37:50 Bye!
