SIG: Go SIG
Date: 2025-08-07
Duration: 54 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 02:28 Hey!
**Robert Pająk** 02:32 Hello!
**Tyler Yahn** 02:35 How's it going.
**Robert Pająk** 02:39 Doing good. How about you?
**Tyler Yahn** 02:41 Doing? Well, yeah.
**Sam** 02:44 Hello!
**Tyler Yahn** 02:45 Hey, Sam, how's it going.
**Sam** 02:47 Good.
**Tyler Yahn** 03:05 Yeah, we could probably get started here in just a second.
If you haven't yet. It looks like everyone has. Add your name to attendees list. If you have topics you want to talk about.
you can go ahead and add them as well.
And then, yeah, we can jump in here. So 1st up, I want to talk about the Ec. 2 detector. It's I'm glad Alex is actually on the call. So there is a Pr from obviously renovate that's not going to work because it's trying to do an upgrade.
This isn't the right. Pr, I don't think maybe it is. I thought there was another one. But anyways it's trying to do like an upgrade to.
Oh, no. Sorry. Yeah.
Reloading. So this is the right one. So it's trying to do an upgrade. And this upgrade is finally deprecating the the SDK, and in the process all of these, you know, imports are failing our lint check because it, you know, should given. It's all deprecated.
So there's already a solution to this that Alex has been put together here a while ago long time ago. And it looks like I'm blocking this.
**Robert Pająk** 04:21 I think we wanted to have as a separate v 2 module.
**Alex Kats** 04:25 Oh, right.
I think that one's that one's merged. I think I think this is the one that's kind of in the original. Before we decide to duplicate.
**Tyler Yahn** 04:34 Yeah, I think that the issue was that there was changes, right?
The fun. Oh, yeah, function. Signatures that were exported were being changed here.
**Alex Kats** 04:43 From the b, 1, yeah.
**Tyler Yahn** 04:45 Yeah. And the problem is, this is also like and it's a stable is kind of the problem. So we so we do have a v. 2 of this already merged.
**Alex Kats** 05:03 Yeah, that's right.
**Tyler Yahn** 05:10 Sorry I don't quite remember. I mean, there's definitely this, yeah.
**Alex Kats** 05:17 Yeah, it should be in the detectors.
**Tyler Yahn** 05:20 Oh, sorry. This isn't the detectors. Oh, sorry. Yeah, that's why I'm confused, all right.
**Alex Kats** 05:32 Use it too.
**Tyler Yahn** 05:35 Oh, it is okay. Sorry. Yeah. Thank you.
Okay, so this is already merged.
We have a v 2 support. This is trying to.
so is the idea. Then we just want to deprecate this module here. And then we could say, Move to the V 2, same as aws.
**Alex Kats** 05:57 I mean, yeah, I think so. I don't know what the right way to handle this is, considering it's stable.
Yeah?
Oh, I mean.
And it shouldn't be used anymore.
**Tyler Yahn** 06:08 Yeah, if it shouldn't be used then, and we have a solution forward for a v 2. I mean, that's how v, 2 s. Go, I guess. So. Yeah, I think that that seems reasonable.
I do wonder how the long term strategy of this do we get like like the issue is also like is renovate going to keep trying to update this? Can we like delete this after we deprec like, get a deprecated release out, I think is the idea?
**Alex Kats** 06:30 Yeah.
**Tyler Yahn** 06:30 Which I think is possible. So yeah, I think think maybe we do. We do that path. So the yeah, I think that makes sense. Alex, does that make sense to you?
**Alex Kats** 06:39 Yeah, that's what I was thinking. I think one way or another, probably shouldn't exist anymore, at least in upstream.
**Tyler Yahn** 07:15 Okay, I will put this in an issue.
And then maybe even just start working on it.
Okay.
cool, awesome. All right. That was a lot less painful than I thought we were. Well beyond what I thought we were on that one. So okay, next up, Robert, you want to talk about minimum severity and trace space, logger configuration parameters.
**Robert Pająk** 07:43 And how does it match for the logger configurator? So Tyler especially, please feel to step in and clarify anything I I will say, because this will be basically the summary of our Tuesday's conversation that we had.
So basically, I will try to summarize everything.
Currently, in the locks seek as well as kind of a configuration seek. There's there is a desire to put to the declarative configuration kind of a way to set a minimum logging severity to the declarative config, and also some kind of idea that the sampling per sampling of logs defined by the trace, sampling or filtering by the trace sampling.
So basically, there are 2 Pocs. How would you be done? So this. So this is the proposal which is more favored by the kind of end users. It looks more better from the user perspective of people reading the Yaml file. So basically, there's something called a default configuration for something called logger configurator. What you say that a default there is a for example, a minimum severity, and that for some loggers with white card matching you could define different. You could define other minimum severities.
So the thing which I wanted to discuss here is basically even that it is favoring. We are favoring this declarative config. There's also a counterpart called logger configurator in the SDK.
There is a hyperlink in the docs. If you can open Tyler just for clarity here, this one.
So this is a concept brought by Java mostly, that they kind of put one to one translation of the declarative config to the SDK, so basically, they want to model all of kind of they want to implement all these things in the in the SDK the same way, almost as in the arm in the arm file.
And me personally, and I think Tyler as well do not like to have this kind of concept in the SDK because we know that it is possible to achieve the same functionality from the declarative config using the processors.
So basically filtering by the logger using the logger processor and filtering, for example, by the logger name is what could be done, for instance, and we our, we would.
Yeah. So basically, I would like just to confirm, and because I would like to give feedback on this proposal that the go seek is fine with the proposal of the declarative configuration, but we do not intend to implement it in a way this kind of declarative config in a way that will implement the logo configurative, this decay that will basically implement it internally using processors or basically choose our own way. How we want to implement it.
that in our opinion, and also probably I would also propose a change in the SDK.
That logger configurator is optional, that the sdks are not forced to not forced to implement it, because right now it's not written. Anyway, if the SDK has to has to basically implement logger configurator, or is it optional?
Yes. So. Tyler, do you want to add anything on what I described? Or do you want to clarify anything.
**Tyler Yahn** 11:32 No, that looks good. I I agree I was I was wondering. This is interesting. I just noticed this, that there's like this section here for logger configurator. I feel like that could be taken out. I don't know why that's here.
yeah. I'd be interested to understand that a little bit more like I feel like that could be removed from this. And if that's the case, then like just having this seems like expected.
I wouldn't want to put this in the in. The the configuration, I guess, is the only thing that I see
**Robert Pająk** 12:14 I think it's also similar to my initial con comment. Or maybe it's still the same one or as a Ps.
yeah. And I said that if we're looking for simplicity I would propose the default config, setting on a several logo provider. So I also had this feeling that this kind of.
**Tyler Yahn** 12:34 Okay.
**Robert Pająk** 12:35 That is very artificial, this thing so maybe.
But I think this this can be discussed separately within the configuration secret, or you do not think so.
**Tyler Yahn** 12:46 Seen a Pr. For this anywhere, so I don't. I don't know
**Robert Pająk** 12:50 Because it's a it's a draft or yeah, it's a specification but this, I think this kind of model is already there for the conf in the scheme, if I remember correctly, I think this logger configurator. Yes, I think it's already there. If I remember correctly.
**Tyler Yahn** 13:10 Okay,
**Robert Pająk** 13:13 Schema, for that's in kitchen. You think.
**Tyler Yahn** 13:18 Everything. Is there?
Yeah, processors, limits.
**Robert Pająk** 13:26 There's it! Is there? 1, 6, 9.
**Tyler Yahn** 13:33 Okay.
Yeah. Alright. Well, then, maybe that needs to not be there. I don't know why.
Oh, I see why?
Because it's beautiful.
Yes, development.
Yes. Development. Okay. Alright, I could think about that a little bit. Then, yeah.
**Robert Pająk** 13:53 Yeah. But then should be only development or logo configure development, because I think the intention is that later we will just keep the development suffix. But the logger configurator would stay. I think that was the intention of the demo.
**Tyler Yahn** 14:06 That is, it is. But the problem is is like, if if you wanted to remove this one level up, then it would be at this tracer provider right.
**Robert Pająk** 14:15 Yes, logger, provider or tracer.
**Tyler Yahn** 14:17 Log. Yeah. Sorry logger provider, and there's no like signal that that section is going to be development, you know.
like, right now, like, you can see that anything under underneath this is going to be in development right?
But if you get rid of this, there's no scope saying that all this stuff is still like in development.
**Robert Pająk** 14:39 But I was thinking, only saying development, and you know.
just removing the logger configuration slash, or you think that it won't work.
**Tyler Yahn** 14:50 Well, that's not yeah. That was kind of like, if you're gonna move development. That would have to be like logger provider.
**Robert Pająk** 14:56 No, no, no, no, no.
**Tyler Yahn** 14:57 Development.
That's how like, yeah, I'm saying like, that's how the configuration Sig is defined like these. These fields is like, I see the like the field itself. There's not like a a blank field. It's called development, at least not yet. Maybe that needs to exist. I don't know.
**Robert Pająk** 15:15 Yeah.
I think it should, because otherwise, how would you add, you know, just new fields that will be in development.
**Tyler Yahn** 15:24 Hmm, yeah.
The idea is that like, I guess maybe it would be like default config forward slash development loggers forward. Slash development, I guess was how how that would match the pattern. That's that's been implemented here already.
**Sam** 15:41 So I wonder do they keep that logger configurator after development is removed?
**Tyler Yahn** 15:49 Yeah. And that's the whole thing that we were we don't want is is, yeah. After this becomes like stable. This would. Then this top field will just become logger configurator.
And that's not really ideal.
Yeah.
okay, so I think that's a a maybe a byproduct of like what you're talking about the Robert, though, because, like we can.
**Robert Pająk** 16:16 Yes.
**Tyler Yahn** 16:16 Just talk about like not having this as a default implementation, and it will help motivate this conversation as well about the configuration structure here. So yeah.
good thing to call out, though, prior to stabilization. So yeah.
yeah, okay, any other topics on this one. Robert.
**Robert Pająk** 16:38 No, that's it.
**Tyler Yahn** 16:44 All right. Yeah, that's a tricky wicket, as Ted would say. Okay. Alex, Sqs context propagation. I'm guessing this is the one where it's not using. Yeah, not x-way. Okay?
**Alex Kats** 16:58 M, yeah. So I guess just want to get kind of the group's opinion on this. So for for one, this seems to be kind of like a spec gap. In my opinion, like there's nothing in the spec that defines anything like any. What Sqs context, propagation should look like outside the scope of X-ray. So it it looks like a few of the other Sdks have something implemented for this. I think Job and Javascript for one where they essentially just write the context to like messages themselves. So I think this is kind of trying to follow suit in a similar fashion. But one. Yeah, just I. I I I guess 2 questions like one, are, would we be okay implementing this? Considering it is kind of like a spec gap, and we're just kind of following suit on a few like reference implementations. And 2, would we be willing to kind of maintain it internally?
Oh, and I guess the 3rd question is, we actually do. Also, it looks like the the person who opened this proposal.
I did also create like an example of actually not having as a context propagator, but just directly within the scope of the aws instrumentation.
That's another option. But that seems kind of less flexible.
Yeah. Just wanted to put put that out there. Kind of get some opinions.
**Tyler Yahn** 18:20 Yeah, I spent probably an hour trying to look into this. And I'm not exactly sure. Yeah, because I think you raised kind of all like touched on all the points like, I think this is probably the original.
Yeah. And then it was like, kind of message mentioned here, that like, yeah, you could just do this with the SDK, some sort of sqs, and then it could be like some sort of, I guess.
wrapper around it. But I think that that would also mean that like any sort of receiver would have to do the same thing. Yeah, okay.
so yeah, I was like kind of trying to follow that I did. Also, I took a look there was like, yeah, I was kind of confused as well about like the semantic conventions around this.
it seems like you might have also taken a look at the semantic conventions for messaging here.
**Alex Kats** 19:08 Yeah, look, there's a part of the spec that talks about X-ray content propagation or Sqs specifically. And then it's it's only within the scope of X-ray. It it pretty much assumes you have X-ray enabled.
**Tyler Yahn** 19:19 Okay?
Yeah. So I guess I'm I was like a little concerned about like the format.
and like the cause, like, I mean.
there. There had to been something.
**Alex Kats** 19:34 Yeah, I, for one, don't even really know how I feel about writing context to the messages directly like that seems like an empty pattern.
But.
**Tyler Yahn** 19:43 Yeah.
**Alex Kats** 19:43 Yeah.
**Tyler Yahn** 19:45 I'm kind of with you on and like, it seems because, like one like the all of the W. 3 C. Issues that they tried to address like come back into play. But they're worse, actually, because, like, like, How do you handle collisions? How do you handle like all these like, you know, formatting questions like I I don't know. I was a little bit like confused about the whole thing, though, so I didn't.
I didn't really say anything, because I haven't fully understood the problem, I guess. And so I guess I was trying to figure out like where this is going. I do think that like one of the things that you just mentioned is that like, if there's other languages doing this like, are they doing it in the same way?
**Alex Kats** 20:26 Yeah, exactly.
**Tyler Yahn** 20:27 Right, like the whole point is interoperability. And like, if that's like, if it's not like, it's just kind of like. Oh, well, I did I do it the Java way, and I do it the.net way. And like those are 2 different ways. It's like.
Okay, now, now, where are we at like?
So yeah, I wasn't exactly sure about this one, either.
**Alex Kats** 20:50 Yeah, I was thinking, is it worth maybe bringing up bringing this up like the specs?
**Tyler Yahn** 20:56 So.
**Alex Kats** 20:57 Good fence.
**Tyler Yahn** 20:57 Yeah, I think that's good. We could do that. I'm also like, I wish we had somebody from aws here. Still, like cause like it's, it's it's a proprietary like pipeline, like. Obviously, this is more universal. Given, it could just be like a messaging system in general.
yeah, I mean that being said like, I'm pretty sure like there is a pretty like Kafka is another one that like we've we've tried to tackle.
**Alex Kats** 21:24 Exposes like metadata in a lot more flexible way. So.
**Tyler Yahn** 21:30 Exactly.
**Alex Kats** 21:31 On! There!
**Tyler Yahn** 21:32 Yeah.
So I don't.
**Sam** 21:35 Implementation. I I saw. We only need to implement the carrier. We don't need the applicator.
**Tyler Yahn** 21:44 Yeah, that's another thing. I was a little bit confused about But yeah, cause the propagator just seemed like it was like a just a.
**Sam** 21:52 Yeah, it's like new key value pair. You can propagate. But I look at the the implementation. It doesn't. You just use the original one with Wcc. Header.
**Tyler Yahn** 22:05 Yeah, exactly like you see something to to hold the data right? And and to return the data in the same form as the carrier, I think, is the more important thing.
**Sam** 22:13 Yeah.
**Tyler Yahn** 22:14 But yeah, but then it comes back to like, you know, is this, yeah, like, it seems like this is trying to set this in some sort of like definite form. And I'm not exactly sure.
so yeah, I don't know. I do think that it'd be like, do we have any like.
Have you looked at Docs for aws on this Alex.
**Alex Kats** 22:37 I mean, I've I've looked at several examples that try to do some like there, there's a few blog posts about this. But there. There's nothing that they expose. They don't expose any sort of metadata, like all of the metadata that they generate is generated internally.
So that's kind of the that's the issue with him.
**Tyler Yahn** 22:54 Yeah.
so yeah, I mean, I think to your point, like, yeah, maybe the specification. But probably a better Sig is the just, the semantic convention, Sig, and asking there, because that's where this is going to get codified. If it does get like, put into some sort of standard we want to follow.
So yeah. I also wonder trying to think who is from aws still,
**Alex Kats** 23:21 Anthony. Let's see from.
**Tyler Yahn** 23:23 Yeah, I don't know how active. I don't think he's active at all in the semantic convention sake. I don't. I don't know. I mean, obviously, I guess we could reach out to him on slack. That's good. Yeah. Maybe maybe that's the way to do it.
yeah, actually, that might be the way to do it. So yeah, I might say that like asking the semantic convention sake for some guidance here, and then asking maybe directly. If aws has like a like preferred way to do this cause like that'd be another thing is like it'd be nice if.
**Alex Kats** 23:51 Like they supported it.
**Tyler Yahn** 23:53 Yeah.
**Alex Kats** 23:54 1st hand. Yeah, see? Like that. That's that is the real solution, like, that's how it should work. But that's a a tougher thing to tackle.
Cause I I yeah, I'm I'm not crazy about writing the messages that like writing it directly to the messages. That that's just not. There's a reason that you expose things like metadata for that reason. So yeah, I don't know.
**Tyler Yahn** 24:14 Right? Yeah, I mean, that's exactly like you're gonna go change the message and then downstream. They aren't using any sort of processing or context propagation. And now the message body is just interpreted as might be like that. Yeah, like, exactly. Yeah, little off.
So yeah, I mean, I, they may already like have this like internal, because I know that they have like. I mean, they definitely have, like telemetry systems internal to the Aws systems, right? So like maybe exposing. This isn't as maybe there's already something there. Maybe it's just not in the like the client sdks, or something like that, like I don't know.
and I'd like to know, though, so maybe maybe we should try following that up.
**Alex Kats** 24:53 Yeah, I could also bring this up like through our internal channels. Aws, directly. Maybe maybe that's a good starting point.
just to see if, because I I the ideal solution is to report it firsthand with an Sqs.
**Tyler Yahn** 25:07 Yeah.
**Alex Kats** 25:08 Yeah. And they do support already for ducks, ray headers, so they should support it for.
**Tyler Yahn** 25:20 Okay.
who are?
Oh, whatever.
Okay, looks like there's already a yeah. Well.
that, I guess, happens when you don't.
Alright, cloud.
Oh, no, this is something. This is not aws. Okay.
yeah. Alright. I guess that sounds like a good plan.
Thanks for reaching out on that one, Alex. I'm interested to hear what's what the what they say to you on that one.
**Alex Kats** 27:13 Follow up!
**Tyler Yahn** 27:14 Okay.
all right. Next up, I wanted to check in on our milestones, hopefully trying to progress towards another release. So we've made some pretty good progress this past week. I don't think there's too much left here.
The main, overburdened right now is just this adding cardinality limits as a stable feature. The next big issue, I think, is this unit testing for cardinality limits you have. Jenny is working on this. I see Alex or Robert shaking his head. So yeah, I think that that's up. Next update documentation for cardinality limits. I think this can be done in parallel. I don't think this is blocked by the unit test. So that's something. If somebody wants to pick it up. I see there's a comment on it.
Don't just yeah, cool. This is just something from from the rustic as a framework. So yeah, this is looking for an owner and then deprecating the SDK metrics X features supporting cardinal. So this might be blocked by the testing.
so there might be a dependency on this. But I don't know exactly.
But yeah, I think that we're just looking, I think for help on this one. And then this is just waiting for a Pr. From the owner, and I think we'll we'll keep going. So making progress.
Otherwise. There's this optimizing id parsing, and string functions. I don't know if this is required for this change. I've looked at this a few times. It's pretty complex. I think Damien was helping review this, and or maybe not.
There's lint issues.
There's an ask. Oh, that's right.
It was asked for Damien to review this. But Damien is definitely not going to be reviewing that and let's see.
yeah, I definitely think that there's some.
This is a pretty complex pr, so I'm not exactly sure it needs to get included in this release cycle. But it's there, and if we need to bump it, it's the only thing left. We can bump it out. I think.
any other things we want to talk about about this milestone, any other issues that we want to add to this milestone that we are, you know.
forgetting.
Okay?
Then we could all take a look, contribute so and contrib.
We've got most of it done. Oh, I forgot to mention our clo stuff was all done. Just that's pretty cool. I don't know, actually, if this has been updated yet.
But yeah, we've got. I got the store card hasn't changed so essentially like what we've done is all the stuff in in the Clo dashboard. We should have everything there except for I think it dependencies manifest. But I don't think that applies. So yeah, I think, like, we've actually done a lot of this stuff. So it's a lot of really great work to help, you know, make this accessible from the community in a lot of different ways, from developers to security researchers to just Pm's, or something like that. So yeah, yeah, just calling that out is pretty exciting. Happy to happy to made it through that.
Okay.
Then, going back to the milestone and contrib. So the last stuff is just this minsev severity stuff. So it was asked to support. You know these ways that you should be able to parse severity from environment, variables, or config, which is pretty helpful. Given like this is going to be useful from the bridges and making sure that, like we could do this in a no code fashion, meaning that you could parse it from environment variables. If you wanted to set up your application that way. So this is the Pr that's addressing that. It's just adding implementations for severity and severity. Var to implement stringers and marshalers and appenders. Now, I guess as well. So yeah, I think this is just looking for more review. I can go over this. But I think it's yeah. It's just looking for more review at this point. It shouldn't be too complex.
I get. Actually, I take that back. I guess there's a little bit of complexity here because what it's doing is it's actually supporting kind of it's supporting the log slog syntax for its parsing of severities. And it's you know, it's emitting of severities. So what this is doing is, if you take a severity that's known, it should just produce that known value ideally, without any suffix of a number. If you are on like a, you know worn one, it should be worn is the idea. If it is, you know, a severity that's in between these like fine grain severities like it'll include that as a suffix. But then there's also this idea that, like what happens if you get a severity that's outside of, like the defined range in this package.
and it follows the syntax of slog here, where it uses these plus and minus symbols on top to show like additional things. So essentially, it's an open ended system. You can put in whatever severity you want at that point it works both ways, both encoding and decoding.
And so, you know, if you try to do some sort of decoding with Json, or some sort of text decoding, it should be able to parse these things.
Put some pretty decent comments, I hope. Hope it's pretty clear when you do the review. What that actually looks like. And yeah, it's taken a lot of this as a lead from Slog. I think if this is a more useful situation than just returning errors or dropping things, I guess, is is the idea. And that's just because, like one, we we don't have like a an undefined severity which I think is ideal, for, like the bridge conversions we default to info. And so when you want to actually like parse these things, I think you want to do it as best you can. The the user is going to likely be doing some sort of like offset. So like in slog, we know there's an offset between the levels and the severity here. And it's a constant. So it should be a really easy translation. So if they wanted to do a string, that's like, you know. I know that I want info, but I know that the offsets also, like, you know, plus 8. So I'm just going to do info plus 8. It should be able to parse that no problem here is the idea. So it makes it very easy from a user's perspective.
In translating from a scale they already know, with some sort of scaling factor, without having to go into this repository and finding out all of those scaling factors. But.
Robert, yeah, I see you have a hand raised.
**Robert Pająk** 33:53 Yeah, I think I'm sure it's worth calling out. There's this one special kind of case, that when it is, I think in between plus one and plus 3. You're not adding the plus right, because these values are defined in the hotel in the hotel.
**Tyler Yahn** 34:12 Yeah, for when I'm the string value, you mean.
**Robert Pająk** 34:16 Yeah. So if this is yeah, so it is info plus 2, it is info 0 3 0 3 info free. But it is more than you're giving this, plus 6 to explore, etcetera. So I think it's worth that. This, you know, plus 6 etc, it's and minus is only below below and above the the ranges, right defined.
**Tyler Yahn** 34:41 That's for that's for when it's encoding. So yeah, so when it's when it's outputting it from this package, it will try to avoid this, plus syntax as much as it can. If there's a defined value, it'll use that first, st and if there's an even simpler value we'll use that. The inverse isn't true, so it'll try its best to accept very complex things. So if you gave me like.
yeah. So if you gave me info 3 minus 10. It'll try to parse whatever that should be is the idea. And so you should be able to give it more than what it's gonna try to provide things that are very standardized except for things that we don't have numbers, for then it will do that. So yeah.
**Robert Pająk** 35:18 And if I remember correctly, you were also kind of explaining it in the comments in the parse function. But maybe I'm wrong, because yeah.
**Tyler Yahn** 35:27 Yeah, it's all. It's all there. Yeah, it's it's definitely the Parse function definitely talks about this here for sure in in the idea that.
**Robert Pająk** 35:35 Excellent, more exactly.
**Tyler Yahn** 35:38 Right? Right?
Yeah. And so, yeah, and but for for outputting, we try to output as standardized as we can. Obviously, whatever it outputs, it should be able to parse, and it does, but it parses more than what it outputs. Is the idea.
So yeah.
**Robert Pająk** 35:57 Could you refresh the milestone? Because, I added the second Pr, which also, I guess.
I'm not sure how it is kind of real So I did this conversation. That look attributes. I think this kind of was also requested by the same user. I guess it is Alex, colleague, because I think he's also working in capital one.
So I thought that including this also in one milestone, could be helped.
**Tyler Yahn** 36:29 Yeah, let's talk about this 1 first, st as it's related to the severity, and then we can jump into that afterwards.
Sure.
So related to that mint severity. One of the things that we don't do is we we just like right now.
define the severity, and if it doesn't match something in the log severity. We'll just give an undefined, but we know that there's like a scale. And so the idea is also proposed. After this min severity, like text interchange is passed. Try to do some clamping essentially, if it's below a trace one. We know that like they're trying to get it to be a trace one, or we don't know. We assume they're trying to get it below a trace one, or if it's above a fatal 4, we assume that they're trying to like, turn off all logging. So try to just provide. That is the idea. Instead of returning an unknown and give a better guess, I guess as to what they're trying to do, and then, otherwise, like, we'll just do a some sort of clamping. But this is something that's just going to be a follow on to the the changes here. It's not blocking in any way. It just helps the user again with the usability of the project.
Yeah.
and so on. That note the usability. Yeah, this is something that Robert just also added, this is a Pr, it looks like.
**Robert Pająk** 37:43 Tyler. So right now it is not doing. It is just returning the original value which could be under and below the range, or it is returning undefined.
**Tyler Yahn** 37:52 Oh, it's a very turns undefined for unknown values. So if there's no mapping so essentially like, if this yeah, if if this if this would, if this conversion right here would return a severity that's not defined in the logs package, and it returns the logs undefined instead.
**Robert Pająk** 38:07 I see?
Yeah, which is.
**Tyler Yahn** 38:12 I mean, it's not wrong behavior, but I don't think it's as as like user friendly as we can make it.
**Robert Pająk** 38:20 I agree.
**Tyler Yahn** 38:23 Okay.
So, Robert, you wanted to talk about this, what is this is we're fixing this issue. So this also probably needs to get in this mouse.
**Robert Pająk** 38:33 Not really fixing, because I think it is helping to fix this issue or to handle it, because right now, if there are field, you know, attributes passed to the logging libraries.
for example, using the semantic conventions, they'll be right now just ringified. So this basically adds support. So we are basically when we have this converting function used in the logging bridges, we have this, you know, we are just checking the type integer. We are changing to log integer, etc. Etc. So I just 2 more types. To this checks one is the log attribute. So people would add just a log attribute to the to you. Note, for example, to the S log or the attribute from the attribute package, then it will also handle basically it will convert it.
So yeah, that's basically it.
**Tyler Yahn** 39:35 I see
**Robert Pająk** 39:40 Soon.
People could basically, you know, use add, you know, attribute values into, you know, S. Log, or the intention is that people that I think the author wanted to use the attributes defined in the semantic generated by the semantic convention tooling, which, in my opinion, makes sense.
**Tyler Yahn** 40:04 Yeah, that makes sense.
What about? So this is getting lost where the conversations were? So one of the other asks, though, is that the he was here like he wants something more than just he wants to be able to convert.
Yeah, like multiple values right?
**Robert Pająk** 40:34 I'm not convinced how to do it nicely, and if we need to do it, need to do it right now.
It says some simple function that I I'm not saying that we should not do it, but I also not sure. I'm not convinced that we need to do it. That's why I propose. I just propose to postpone this decision, but I'm open to any other feedback, and you know opinions here.
**Tyler Yahn** 41:01 Yeah, I mean, I honestly, I think this should exist in the Go Standard Library.
like disability. Like, if you can just translate an element of a slice, you should be able to translate the whole slice in some like function. Call.
yeah, it's there. It's not hard to like. You're right. It's not hard to do, but it's also not hard to do generically like.
So it seems like.
In fact, I was looking in the Standard library and in the experimental packages to try to find something for this. But I couldn't find it.
**Robert Pająk** 41:35 You're right that it might be added in future into S. Lock. And then our functionality could be redundant. Right?
**Tyler Yahn** 41:42 No, I think it should be added to the slices package. Yeah, it's like the snow.
But yeah, that's that's where I was anticipating it. But I think that, like.
I think we could provide something like this. I just don't know where we would want to provide. It is the idea, because, like, I see their point like and just like this is kind of annoying like, when you have to do like this.
this, this thing here. It'd be nice if it could just be a single line.
I mean, because, like, we could do this like this providing some sort of like map function here, I think, is totally.
And this is something I think, that needs to be in the Standard Library. Really.
I just don't know where we would hold. This, though, I guess, is kind of the question.
Is this something that we could put alongside the the the conversion function between like common attributes into the log attributes.
No, probably not. That doesn't make any sense.
**Robert Pająk** 42:53 So the reason I will postpone it, because it might eventually, you know, put into the slice package in the Standard Library. So yeah, I'm not sure we need to do anything right now.
**Tyler Yahn** 43:11 Yeah, okay.
**Robert Pająk** 43:13 Unless there is more feedback. You know people asking for the same.
**Tyler Yahn** 43:16 I mean, I think that like it seems like in the slog package, we could at least do something like you don't even need to do generics you could just put in like, yeah, hotel slog, like.
I don't know if I'd call it this. But maybe something along this line, right like you could essentially just provide like a single implementation of that.
**Robert Pająk** 43:37 Yeah. But then, would you want to do the same for all the bridges or logras, you know, as zap logar, etcetera.
**Tyler Yahn** 43:50 Yeah.
I mean, unless we could find a centralized place to do it. But I don't know of a good one like I mean.
outside of just doing some log utility package which I really don't want to do.
I mean, it's the same reason, like like Bogdan was asking about like that conversion of attributes to to log attributes right? Like it's just a simple function, right? Like it's it's not. I guess it's kind of like a 20 line switch statement. But like, it's just a function that you could write every single time. It's just that.
Think myself.
**Robert Pająk** 44:29 I think Bogdan asked was different. He just wanted us to use attributes.
**Tyler Yahn** 44:34 You just wanted to use what.
**Robert Pająk** 44:36 I I think that he was he would just wanted to. I think that he didn't understand why we didn't use attribute for modeling clock attributes. I think that.
**Tyler Yahn** 44:46 Well, yeah, I I think that's fair.
**Robert Pająk** 44:50 Yes.
**Tyler Yahn** 44:50 A whole other conversation, but.
**Robert Pająk** 44:53 I think these were just our hack to provide. You know, this function. This is how I see it, but it's not an ideal solution.
**Tyler Yahn** 45:02 Yeah, I I got you.
But I I think that like, okay, if if that's the case, like, I think that somebody's using the hotel slog. I don't think they're like, if every user is writing this function and we could provide it as like a 1 word, like a 1. 1 line conversion form like that seems to motivate it right like it's not hard, right like
**Robert Pająk** 45:31 Yep.
**Tyler Yahn** 45:32 I think it's worth adding. I don't know if it's worth adding to every bridge, because I mean also like it may be that you have. Every bridge may need something else slightly different, right? So that might actually motivate doing that to every bridge right? Like, maybe this function looks different in in one versus another.
Yeah, but I don't know. I have to take a look.
I think that you're so that being said, your Pr. I don't think is blocked by that. This conversation. So maybe.
**Robert Pająk** 45:58 No, I think it's still, and I think it's still enabling it. I think it's still.
Yes, yeah.
**Tyler Yahn** 46:03 Yeah, a hundred percent. I think I think that's fair. Yeah. So.
**Bryan Boreham** 46:08 Yeah. The.
**Tyler Yahn** 46:09 Go ahead!
**Bryan Boreham** 46:10 Sorry. Just wanted to interject that those those functions worry me on a on a performance basis particularly, because they're they're doing a lot of memory allocation, even in the case that you're gonna drop that log line because you you have Debug logging, turned off. Say.
so. I would. I would rather see the thing, see it like a type which goes through, and then, when it's needed, turns into a string rather than call a function at the top level, which is like, I say, that that forces the memory allocation, even like, even when you're not going to need it.
**Tyler Yahn** 46:51 So would using a sequence be something that you're talking about, something more like this.
**Bryan Boreham** 46:56 Maybe.
**Tyler Yahn** 46:58 Or you're talking.
**Bryan Boreham** 46:59 I I didn't manage to read the detail of all of that, but they
**Tyler Yahn** 47:04 Yeah, I, yeah, obviously, it could be a a little bit. But even here, like, it may not be a hundred percent, because this sequence may just get flattened. Yeah, if you pass in, what what was I doing here?
Yeah. So like, it's already just collecting the the sequence. So like this is flattening into something. And if it's just being called all the time to to flatten that into some sort of like memory space, then yeah, that that may not be ideal. So what you're saying is more that, like
**Robert Pająk** 47:36 I think that, Brian right now. The only way to not have this over unnecessary overhead is to use the the enabled function to check if something on a given lever and context will get emitted and have this this kind of if block.
**Tyler Yahn** 47:54 Oh, I see what you're saying.
So you're saying that like, yeah, that's I see what you're saying, Ryan, or Robert like.
Instead of doing this here, you would. You would 1st wrap this in some sort of enable and see if it's gonna actually get called or not.
**Robert Pająk** 48:10 Yes, exactly. I think it's also it's more in the goal, imperative philosophy, way of coding.
**Bryan Boreham** 48:19 In whose philosophy.
**Robert Pająk** 48:22 I mean go programming language where it is mo, mostly, you know, imperative language when you do not have, you know, a lot of lazy evaluations, etc.
**Bryan Boreham** 48:32 Yeah, alright. Anyway, I I that's my opinion. That's my reaction.
**Tyler Yahn** 48:39 Well, so I mean, yeah. And I think to Robert's point like that, it's explicitly a part of the slog package, right? That enabled function, and I think that that's something that makes a lot of sense in slog.
I don't know if that's the case in other logging bridges, though.
**Robert Pająk** 48:54 It's make. It's also in that.
Okay, it's also Logras.
It's it's not.
**Tyler Yahn** 49:00 Log, r.
**Robert Pająk** 49:03 Think it is as well if I remember correctly, there's also enabled in logar.
**Tyler Yahn** 49:09 I don't. I don't. There's definitely I don't think it's universal like I definitely think there is at least.
**Robert Pająk** 49:13 It's not that universal. I don't think it's that universal, but I think it covers the severity level.
Let's see.
**Tyler Yahn** 49:22 Yeah, sure, but I don't. I don't think that, like all of our bridges, have an enabled method, though, is the thing.
**Robert Pająk** 49:28 Yeah, I think they have. I think they have all of them.
**Tyler Yahn** 49:35 Okay, I don't think we maybe don't need to go into it too much here. But like, yeah, I think to Brian's point that like it may actually make more sense to do this on a bridge by bridge, because there may be places where like.
if that optimization needs to be done like we could, we could address it in that one where there isn't some sort of enabled. Right?
Yeah, so yeah, I think, looking at that and trying to understand it from the memory. Allocation for for these sort of like calls is important. But yeah, I mean also to to Robert's point, like.
I think that's why it was designed to have an enabled method. So if you don't want to do expensive operations, don't don't do that. But yeah.
yeah, I also think that there's maybe like a translation layer as well.
Yeah, I don't know like it would be nice if, like, you could string these together, and, like the memory, allocation would just be avoided, because, like, it would really stink if you're trying to do a conversion. But to, you know, from some attribute, slice to some S log slice, then to some log, attribute slice, then to some protobuf slice, or something like that, and just avoid all of these other slices, and just like jump right through the middle. But that might be something we want to take a look at. Actually.
I do know that sequences are very new to the the library and a lot of functions. So it might be worth seeing if we want to try to support something along that line.
That's a good. That's a good question. Okay.
But back to the milestone, I think this just needs more review. If you have some time. Please take a look. This is this is just looking for.
Yeah, more reviews. And then then I think also, if you have more thoughts on this, please comment in this issue here. There's definitely some good conversation. I'll try to capture some of the in this in this afterwards.
Okay, that took way longer than I thought.
Sorry.
so all right. That's the end of the agenda. I'll pause here. Any other topics people want to talk about.
Brian. I know we talked about last time. Grpc implementations. Did you end up talking to the collector, Sig at all?
**Bryan Boreham** 51:59 Not yet. I I went hunting around a bit more.
so I I don't know how interesting this is in general. So the the they're the collector is using a Protobuff generator called Google Proto, which is itself deprecated. We didn't talk about this last time, did we?
**Tyler Yahn** 52:24 We didn't. But we've talked about in the past like we used to use Gogo proto as well. Yeah.
**Bryan Boreham** 52:30 So I I wanted to kind of research that because I, as far as I can tell, they're not using any of its features like.
you know, trying to make it go faster, I'd be going. Gee, I wish we had Google Proto, because it has features that can make it go faster. But they're they're they're kind of on the wrong side of that trade. They're using Google proto and not using the features that make it go faster.
so yeah, I I that's my answer or my status is I wanna research where? Where it's at a bit more before I start asking more questions.
**Tyler Yahn** 53:07 Yeah. Fair. Okay. Well, cool. All right. Yeah. Keep some forwarding on any findings, because I'd love to implement that as well, or or take a look and think about it in the the protogo stuff. So yeah.
awesome.
yeah. Any other topics. We want to discuss cool ideas projects that we're working on in the past week.
Any talks accepted to Kubecon that you can now say that you've got accepted.
**Robert Pająk** 53:40 There was a disclaimer to not say, yet accepted.
**Tyler Yahn** 53:45 No, that was, that was on the 30th of July.
Ask me how I know I got one accepted. So yeah.
**Robert Pająk** 53:53 Same here.
**Tyler Yahn** 53:54 Yeah, yeah.
That being said, I guess that if you haven't yet signed up for the conference I'd love to see you all there. So yeah, try to. I'm planning on being there, so it'd be great to to see you all there.
Probably also the Maintainer Summit as well. I don't see anybody on the call who wouldn't be accepted to that. So yeah, I think like, that's also another thing. If you are going to the conference. Try to sign up for that as well.
Well, cool.
all right. If there's nothing else we can end the meeting here. Thanks everyone for joining. Appreciate your time. I will see you all in weeks, time, or asynchronously. Bye.
