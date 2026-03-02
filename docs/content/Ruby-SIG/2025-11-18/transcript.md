SIG: Ruby SIG
Date: 2025-11-18
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/I1_iWriYQXPUjEw8Xy5fu030QA2XsVAEPLxTlAc8kYvYW1N_IqWirgpoWP77yYQ7.7xGw0MUBQXws3K06
============================================================

## Zoom Recording Transcript

Hannah Ramadan 00:01:42 Hey, Ariel.
Ariel @arielvalentin (ATX, USA) 00:01:44 Hello, Anna.
Hannah Ramadan 00:01:45 How's it going?
Ariel @arielvalentin (ATX, USA) 00:01:47 One day at a time.
Yourself?
Hannah Ramadan 00:01:50 This is the good answer. I'm gonna take that.
Ariel @arielvalentin (ATX, USA) 00:01:58 Hi, everyone.
Hannah Ramadan 00:01:59 Sheila.
Ariel @arielvalentin (ATX, USA) 00:02:00 I'm relocating.
Kayla Reopelle 00:02:03 Okay.
Ariel @arielvalentin (ATX, USA) 00:02:03 So, I've got my camera off a little bit.
Kayla Reopelle 00:02:07 No problem.
Mmm…
I can share my screen. Today's one of those Tuesdays where I can only stay till, quarter of, so…
Ariel @arielvalentin (ATX, USA) 00:02:18 Perfect, it would make the meeting faster.
Kayla Reopelle 00:02:20 Yeah, there we go.
Hey, Alex.
Welcome.
Hold on. Sorry, I'm having some screen sharing troubles.
Okay, can everyone see the notes?
Hannah Ramadan 00:02:51 Yeah, understood.
Kayla Reopelle 00:02:53 Alright, awesome.
Okay, well… Let's see…
I'll add a link to the agenda, just in case anyone, has other things that they want to add.
I am super far behind things. I've kind of been battling a cold and dealing with travel, so I know there's a lot that I have to review, so I'm kind of slowly working my way through that today. Thanks, everyone, for their patience.
Yeah, I guess we can… Start with the Spexig.
Which I was only able to attend part of today.
And the part I was able to attend was at the end. So, this…
random trace flag thing I haven't taken a look at yet.
Sounds like we may have some issues opened to address it.
If we have any pending environment variable propagator pull requests, which I don't think we do, asking to review those.
This log record processor enabled flag,
It's gonna be merged today, and that's something along with the logger enabled that's on my radar to try to…
round out those new spec requirements for the logs SDK.
Always Record Sampler will be merged soon.
Which I guess is maybe, like… Always on…
A sampler decorator.
Well, it doesn't seem…
too difficult. But, you know, this is just kind of merging the initial spec and not marking it as stable, so…
We don't have to work on it right now, but we can if anyone's interested.
Sounds like Zipkin might be deprecated soon.
I know we did have a community member submit a PR related to Zipkin recently.
So, I guess that's something to keep an eye on. If we have less code to maintain, that's always nice.
Okay, this was where I joined, was this,
logging API confusion, it sounds like…
you know, and I face this too, there's…
some uncertainty around whether the logging API should only be used by logs bridges, or within logger libraries, or if people can actually use the logs API to generate their own OpenTelemetry log records outside of any other logger.
Technically, the spec right now does not really encourage people to do this, but in our implementation in Ruby right now, you can. It really doesn't make a difference for how we treat things.
But, yeah, so this conversation, I think, has been had a few times, and is just continuing now.
if you have thoughts on whether the logs API should be allowed to,
You know, just be used directly.
I would… I would chime in on this issue.
It sounds like… Let's see…
So it sounds like, yeah, having a more convenient logging API is likely.
But they… they didn't quite make any decisions today.
This one was kind of just… Glazed over,
OpenTelemetry is trying to get to be stable, so they have some feedback that they'd like from maintainers and contributors to see, you know, how to work on, how we define stable, you know.
the way that we deal with semantic convention stability, etc, so I really recommend…
taking a look at this one and weighing in on it. I think there's some extra energy, since they want the project as a whole to become stable, and clarifying these things will really help.
And yeah, and then just kind of briefly mentioned some other OpenSpec PRs related to entities, and, Wendy's not here today, but, she's brought up a few times this goal of being able to remove,
synchronous instruments, or just really, like, metric instruments in general, and that is getting some traction, so I'll, message her about that so she knows that it's kind of back on their radar.
Yeah, okay, so a lot was in the SIG today, just kind of blazed through this. Is there anything that people want to dive into more deeply during this meeting?
Or should we just continue?
Okay, I'm gonna take silence as a cue to continue.
Alright, we have an issue with the logs and metrics SDK. Yes, I…
saw this, and it's on my list to take a look at today. Has anyone run into this problem where… so basically, like, the require…
is kind of… off,
there's also a PR to fix it, which I think is good, it just might be a breaking change,
Because I think people will have to require things differently.
Which is fine, I mean, logs isn't stable, so we can certainly break things.
Yeah, any thoughts on that one before?
Ariel @arielvalentin (ATX, USA) 00:09:24 I haven't looked at the issue, so I'm not exactly sure what the problem is.
Kayla Reopelle 00:09:27 Okay.
Yeah, I'll have to look more…
Deeply at it, too. My… my sick brain last week couldn't really handle it.
Alright, what have we got here?
Update the cell.
Ariel @arielvalentin (ATX, USA) 00:09:52 Okay, so, Shawana and I have been going back and forth on this one issue.
I think so, right? Is this the one, Shalon, where it's you and I just chit-chatting back and forth?
Xuan Cao 00:10:05 Yeah, yeah, that's all.
Ariel @arielvalentin (ATX, USA) 00:10:08 Okay, Here's the problem, is that…
We don't quite understand what's happening with the runtimes.
Ruby no longer has the…
The thrift gem that we depend on for implementing the Jaeger exporters?
Has conditional logic in it.
So it wanted to remain backward compatible with Ruby 187.
So, it will define a, A class that's missing.
that's introduced in Ruby 1.9.
The class has since been removed.
As part of the language, the standard language, in Ruby 3-2.
Is it 3-2, Swan?
Xuan Cao 00:11:12 You mean with the version that, they don't… but they don't support, the VXNEM anymore?
Ariel @arielvalentin (ATX, USA) 00:11:19 Yeah, it's 3-2 that it was removed, right?
Xuan Cao 00:11:22 I think we moved from 2.4.
Ariel @arielvalentin (ATX, USA) 00:11:28 A fixed number was removed from 2.4.
Xuan Cao 00:11:30 That's what I… Saw wine, cuckoo stuff.
Ariel @arielvalentin (ATX, USA) 00:11:36 Oh, okay.
So, at some point, Fix Num gets removed.
And, in the thrift code, it's, like, looking for a specific version of Ruby where it…
Reintroduces this type that he uses internally.
And then, what we see in the JRuby builds, when we upgrade JRuby to 3-2,
FixMom, that patch doesn't work.
And… fixed num… and what we're seeing is that Jay Ruby's, like, failing because the thrift library
Isn't declaring this fixed norm as sort of like its patch.
and so it shows up as a…
As an error where… I believe a name error where that type doesn't exist, a fixed num class doesn't exist.
We do not see this same error in Truffle or in…
see Ruby, and we don't understand why.
Kayla Reopelle 00:12:46 Hmm.
Ariel @arielvalentin (ATX, USA) 00:12:50 And so, I'm thinking to myself, like, this seems like a problem in the thrift gem?
Whether Thrift is relying on language-specific types to be present, and something isn't getting loaded correctly.
The Rift is not receiving any more updates.
So it's kind of, like, signaling to me that Thrift isn't compatible with our version of Ruby, and we want to try to get to a min version of Ruby
That is 3-2 anyway, so it wouldn't be… Allegedly wouldn't be… compatible?
And we only see this problem because we're upgrading Setup Ruby to get to a newer version, and the builds
In the core repo.
Try to use the latest version of Ruby, JRuby, instead of saying, I'm gonna pin to JRuby, whatever.
Like we do in the contravo.
So…
as part of the, sort of, setup action, so how we got into this situation was we're upgrading setup action, which is pulling in JRuby 10, which supports a minimum of JRuby 3.2,
Which it seems that the Rift Gem isn't compatible with, and shouldn't be compatible with,
I see Ruby anyway.
The thing that we were debating was what's on line 18 here.
Which is… Demonstrating compatibility with JRuby in our test suite.
But that masked the problem, whereas somebody actually tries to use JRuby with Drift, this wouldn't work.
Kayla Reopelle 00:14:37 Yeah.
Ariel @arielvalentin (ATX, USA) 00:14:39 And still, the mystery and puzzle of why CRuby works.
Kayla Reopelle 00:14:45 Yeah.
Ariel @arielvalentin (ATX, USA) 00:14:47 So…
Given all of those constraints, one thing I wanted to know about was, I know that they were talking about dropping support for Zipkin.
as part of the core SDK. Is that true for Jaeger as well? Or do we do a thing where we're painting Jaeger to only be supported because the gem only supports?
Kayla Reopelle 00:15:06 Hmm, yeah.
Ariel @arielvalentin (ATX, USA) 00:15:08 you know, Ruby 3, or whatever it is, right? Like, there's gotta be some decision that happens here.
And I think… and I… and that's what Schwan and I were.
I don't know if we have a disagreement, or we're at an impasse, or whatever it is, but I kind of feel stuck myself.
about what it is that we want to do, because I kind of feel like this solution, Sean, as I mentioned, it feels like this is…
Masking a problem?
That we don't understand very well, and it is…
Making it look like we have compatibility when the gem actually doesn't?
And I want to avoid that problem, if possible.
And again, I don't even know how much it matters that you really supports Jaeger Thrift Encodings.
Kayla Reopelle 00:15:57 Yeah.
Ariel @arielvalentin (ATX, USA) 00:15:58 Jaeger now supports OTLP natively, because they recommend using the collector, right?
And so I don't know what the specification says about our… I haven't looked yet.
Kayla Reopelle 00:16:14 even.
Ariel @arielvalentin (ATX, USA) 00:16:14 Whether or not it matters, like, well, do we sunset this?
And if we do decide that we want to patch this this way.
I would think that it's a patch that's part of the gem itself, that the Rift… the Jaeger…
exporter gem, if that's a…
liability we want to take on, because we're going to be, as part of our gym, introducing a fixed num type, and that's going to change the…
targeted runtimes environment to who to fix them, and it's like, where did that come from?
Why does that exist?
the way that… and, you know, Drift made that decision, I don't know that I agree with it, but…
That's the way that that germ was implemented.
I'll leave it… I'll leave the floor open for…
Kayla Reopelle 00:17:09 Yeah, this is… this is complicated. I don't want to mask compatibility, because I think people, you know, often look at,
CI actions to see what's tested in terms of compatibility.
And it might be hard for them to find this test helper.
I am curious about what OpenTelemetry sees as the future of Jaeger-specific exporters, since Jaeger now has OTLP support. I think that would be helpful to look into, to just see…
If this is something we need to continue to maintain,
I also don't know how many people are using JRuby and Jaeger together, or even how we can find that information out, in hotel land.
So, if thrift… Isn't going to work with these versions of JRuby.
Anyway, though, yeah, maybe we just need to cap.
Our testing, Because, cause, are you saying the thrift gem…
is a dependency of our Jaeger exporter, and…
the Jaeger exporter will still install even on that incompatible version of JRuby. Like, the gem file… like, Bundler doesn't resolve it and be like, oh, you can't use this version, and go backwards.
Ariel @arielvalentin (ATX, USA) 00:18:40 Yeah, because the Rift says any version of
We looked at the Thrift Gem spec.
It's like any version of Ruby greater than this.
Kayla Reopelle 00:18:48 Yeah.
Ariel @arielvalentin (ATX, USA) 00:18:49 and intern… I think I've linked
Some stuff in the file to show where it's doing its compatibility stuff.
Kayla Reopelle 00:19:00 That's unfortunate. Yeah, I don't think we should necessarily.
Ariel @arielvalentin (ATX, USA) 00:19:02 So, yeah… If we look at the core extension fixed numb, if you click that.
It's like my second con… my second URL, Apache Drift there.
So they define a class called fixed numbing here.
For compatibility with versions prior to 187.
Right? And so there… Opening the class and adding org.
Because, sorry, I'll re… re-express what I was trying to say.
Fixnum exists, but the ORD method did not, and they patched that.
However, fixed num doesn't exist in 3.2 or greater. If you look at the removed constants in the changelog for Ruby 3.2.
So it's like, where is this coming from, and why does it work sometimes, and why doesn't it work other times?
I don't know. I don't know the answer to that.
So those are compatibility issues, and I…
I'm concerned, again, concerned that, like, hey, we're gonna go ahead and introduce
Fixed num, as opposed to it being integer in use.
And adding fixed numb in back.
doesn't seem good. So, in a sense, it's kind of like, because we can't fix the rift unless we submit a patch.
Or we patched RIP in our code, as a fork.
And replace the usages of fixed number with integer.
that creates some compatibility, but deviates from the gem that… you hear what I'm saying? It just sounds like a mess.
Kayla Reopelle 00:20:48 In other words, I don't…
It sounds like a lot of maintenance, so I… I think the next question I'd love to know the answer to is, like, what OTEL sees as the future of Jaeger, because if this… if it's deprecating Jaeger, and we can just deprecate it as part of this move, I think that would be ideal.
And if that's not the case, then we need to keep supporting Jaeger.
Then I think… We might just need to remove…
JRuby compatibility, and maybe add a note in the changelog that, like.
Thrift… Thrift has broken this, we are not the maintainers of Thrift, and so we can't continue to support it for these newer versions.
Ariel @arielvalentin (ATX, USA) 00:21:33 I do want to reiterate that it shouldn't work for CRuby either.
Kayla Reopelle 00:21:37 Oh, I see, okay.
Ariel @arielvalentin (ATX, USA) 00:21:38 But it is.
And… to… and to Schwan's point, maybe what we need to do is… like, another option we have
was to explicitly call out that Ruby… JRuby 9 is supported.
If JWB10 is not, and having some sort of, like, constraints in the gem spec that would say that.
Kayla Reopelle 00:21:58 Yeah.
Ariel @arielvalentin (ATX, USA) 00:21:59 But… I'm also trying to get a PR together that's like, stop supporting Ruby 3.
Kayla Reopelle 00:22:06 Yeah, yeah.
Ariel @arielvalentin (ATX, USA) 00:22:07 You know, less than 3-2.
So… And I don't mean to talk in circles, Kayla.
I feel like that's what I'm doing to you, and I'm sorry.
Kayla Reopelle 00:22:19 It's okay.
Ariel @arielvalentin (ATX, USA) 00:22:20 Okay.
And the same thing for Schwan, I'm sorry, I feel like I've been, like, just going in circles with you, so I hope you…
I hope you empathize, understand my position and my concerns.
And, you know, I don't know if you have any…
Other concerns or disagreements at this point?
Kayla Reopelle 00:22:41 Yeah.
Xuan Cao 00:22:42 No, I don't, I don't,
because I was trying to do this kind of quick, because I started just,
something easy to edit. But then, after I look into, like, why it happens, and I think it's more complicated than I originally thought, and if you look at… I think… if you look at my, comments, I do think this issue that
But the different… they have a different call sequence?
I don't really know why, the JWB10+, it just invoked those,
that right type function that caused the issue, but for all the ruby doesn't invoke, it used to transport
I think that's why it works for the CRB.
Because it never calls those stuff, so…
For me, it's still possible that why have different cost increases.
Yep.
Ariel @arielvalentin (ATX, USA) 00:23:49 That Ruby version constant that's in the thrift gem?
Does JRuby publish that value?
So now I'm thinking of 3 things.
The first thing is, there's the check in the Thrift jam that says, open, fixnum, and add a method to it.
if the Ruby version value isn't interpreted, or basically comes up with No.
Does it skip that entirely in JRuby? Second, is there some JIT compilation that's happening?
That's inlining the method calls.
And bypassing some… and that's why it looks like it's taking two different routes.
And then the third thing is that if there's an incompatibility between JRuby and CRuby in that case, is there a bug open for it?
Or is there another C version of a gem somewhere?
That is, inserting the behavior.
Kayla Reopelle 00:24:57 That would cause it to deviate.
Yeah.
Ariel @arielvalentin (ATX, USA) 00:25:04 Anyway… So… In order for us to move forward with this, what do you all think about this?
We create a constraint on the… at least to get the setup will be action and updated.
We changed the JRuby version to be fixed at 9.
We changed the GEM spec to be fixed at less than 3.2,
Because FixedNum, now we know, is not compatible.
And that kind of forces the builds to be maxed out at 3-1 for… the Jaeger exporter?
And we can merge that for now.
Kayla Reopelle 00:25:47 So, the Jaeger gem couldn't be installed on, like, Ruby 3.3 with that approach. You would…
3, 2, or greater.
Okay, so 3.1 is, like, the only version, or below, you could install it on.
Ariel @arielvalentin (ATX, USA) 00:26:01 Yeah, because that has fixed numb in it.
Kayla Reopelle 00:26:08 Yeah, I think that… that could work.
I do think there is a…
Well, yeah, we'd release a new version of the gem, so people would know, and it would be locked, and if someone was getting it to work on a newer version of Ruby, they could go back to a previous version. It's not like we're really changing much inside of the gem itself, so if it was working for anyone…
They would have a way to take care of it.
I think that works. I think being more explicit and kind of taking on that.
version defining to help Bundler do the right thing in our gem is enough.
Ariel @arielvalentin (ATX, USA) 00:26:49 What do you think, Sean?
Xuan Cao 00:26:52 Yeah, I'll… I think I have a hard cap on the J-Review version… review version would be.
Oh, work, yeah.
Kayla Reopelle 00:27:02 Cool.
Ariel @arielvalentin (ATX, USA) 00:27:02 Awesome.
Thank you so much, man. Appreciate you.
Kayla Reopelle 00:27:08 Yeah, thanks, Schwan, and thanks for talking this through.
Does anyone… want to see, too, if Jaeger is still… like…
you know, accepted in the spec, or, you know, if there's any future for Jaeger.
Ariel @arielvalentin (ATX, USA) 00:27:28 I do have some follow-up questions.
about spec compliance and, future.
Ty, like,
meeting agenda item? Yes. So we could, maybe we can address it then, that way we're not stuck here.
Kayla Reopelle 00:27:45 Okay, that sounds good.
Okay, so…
Ariel @arielvalentin (ATX, USA) 00:27:53 Oh, this is me again? Oh, man, I'm sorry, buddy.
Kayla Reopelle 00:27:57 It's all good.
Ariel @arielvalentin (ATX, USA) 00:27:58 So, something that we don't do a good job of is keeping up with proto releases.
Just in general, like, what's not happening is that there isn't…
a project management process between the spec.
Committees and us.
maintainers. It's kind of like, oh, we announce a release of something, and then go and… Do stuff, right?
So, something that I had asked, and got crickets, no responses from folks, is how they keep up with Protos. And I'm wondering to myself, like, if there's something that we can do to subscribe to Protobuff Update, where…
a protobuf… The new tag on the protobuf repo gets… released?
Kayla Reopelle 00:28:39 Yeah.
Ariel @arielvalentin (ATX, USA) 00:28:39 And then that causes a… either opening an issue or opening a PR.
And then we also create a GitHub action Or process that would…
Regenerate the protobus using the latest version of the compiler, Yeah. Using,
using the latest version of the spec, and kind of all of that gets handled by an automated PR.
And then we're able to at least see, oh, a new spec is released, and we're trying to keep up with the protobus of regenerating the code.
Kayla Reopelle 00:29:19 Yeah, I think that's a great idea. I can also go to the spec sig next week and add this to the agenda and ask, since people aren't answering in the channel, though it might be worth pinging again, since people were at KubeCon last week, so I think that might have contributed to the crickets.
But if they haven't responded, I can just ask to see if anyone already has an issue, or, like, an action like that, that we can leverage. If not, yeah, I think automating that, that's similar to kind of…
I hope I have for semantic conventions to automate, you know, when we know there's a new release of semantic conventions, have a GitHub action run the update script for us, so that way we can…
Make sure we stay up to date on that as well.
Ariel @arielvalentin (ATX, USA) 00:30:06 Yeah, so anything that we can do to try to force ourselves into compliance without requiring human beings to do it would be, like.
Kayla Reopelle 00:30:14 Definitely. No, I think that's a… that's a great effort.
Would you be up for making an issue in our repository to kind of track this idea, and then,
I will add it to the SPECSIC agenda for next week, and can report back to you on how that conversation goes. Does that sound good?
Ariel @arielvalentin (ATX, USA) 00:30:35 That sounds amazing.
Kayla Reopelle 00:30:36 Okay.
Cool.
And spec compliance.
Ariel @arielvalentin (ATX, USA) 00:30:53 So we used to go through this process with, I think it was Carlos, who would come through and look at
What we've done, and said, yes, you are compliant, or no, you are not meeting this specification.
And I don't know that we have that process now with, you know, or what…
We're not yet ready for it for logs or metrics, but,
We don't have, sort of, like, this ongoing compliance
Or compliance matrix, or whatever it is that…
allows us to say that the Ruby SDK and the Ruby API conform to what the current state of things are.
Kayla Reopelle 00:31:32 We are compliant with version XYZ of the specification.
Ariel @arielvalentin (ATX, USA) 00:31:38 We're kind of doing that stuff manually, and as new OTEPs are getting added.
We're still, again, just like with the protos, we're relying on humans to do project management.
Kayla Reopelle 00:31:50 Yeah.
So can we automate that process in some way? Can we have…
Ariel @arielvalentin (ATX, USA) 00:31:56 Automated issue creation happened.
in SDK repositories.
Yes, it would be great, you know, Gen AI, be able to look at a spec and be like, hey, what's the difference between these two commits? And then probably make issues, right? Like, that might be a driver.
Kayla Reopelle 00:32:12 I'm not…
Ariel @arielvalentin (ATX, USA) 00:32:13 You leverage agents to do that work.
But, please, go ahead, Kayla.
Kayla Reopelle 00:32:20 This, exact topic is something that they're discussing related to that blog post that I showed earlier about evolving the specification.
Ariel @arielvalentin (ATX, USA) 00:32:30 Boom, that's all my burning questions.
Kayla Reopelle 00:32:32 In the specsig, they… they want to…
kind of find a process for that. I don't know if anyone has taken that on for the community yet as a to-do, to kind of have something that creates new issues for repositories when new specs are merged, or when a new version of the spec comes out.
But this… just to say that this is a conversation that's happening throughout OTEL, and it's not just our SIG that's struggling with it.
Yeah, and I do think we're actually at a place now where I want to engage
The spec maintainers on our logs process, because the only things we have left are the enabled flag.
And the event name. So, I want to make sure we get on their list of,
SIGs and implementations to review, so that we can hopefully bring logs to stability, like, early next year.
So that might also, you know, make connections that can help us learn more about how other SIGs do this, or if anyone else has automation, or just…
You know, make sure the maintainers know that this is something that's really important to us to feel like we can stay up to date.
On the spec.
Yeah, yeah, because right now, it's a lot of manual work to go through and make issues, and…
Everything is kind of frozen based on when you last were able to do the manual work.
I think I'll have more time next quarter to kind of do a full spec audit, but if there's some automation to help us, it'd be great to get to do that before January. If not, then in January, I should have time for it.
Ariel @arielvalentin (ATX, USA) 00:34:22 Thank you, Caleb, appreciate you.
Kayla Reopelle 00:34:24 Yeah, no problem.
Alright, that's it for core for now. Since we have so much on our agenda, I'm not gonna dive into these, specific issues, so let's just keep cruising through. New HTTP PRs? Is that a Hannah post, or an Ariel post? Who added this one?
Or Alex, did you add this one?
Hannah Ramadan 00:34:51 Yeah, that wasn't me, maybe… was that Arielle's stuff?
Ariel @arielvalentin (ATX, USA) 00:34:55 Yeah, I mean, I put… I'd love for feedback on the PRs I submitted, but .
Kayla Reopelle 00:35:00 Yeah.
Ariel @arielvalentin (ATX, USA) 00:35:01 I didn't put that on the list, I don't think.
Kayla Reopelle 00:35:04 Okay.
Alex Arnell 00:35:05 It wasn't me.
Kayla Reopelle 00:35:07 Okay. Cool. Mystery guest. Mystery guest, if you're watching the recording, please message us in the Hotel Ruby channel to let us know what you wanted to talk about.
Okay, review and merge the code owner's PR? Is that already?
to go. I did get some feedback.
From… the guy who made…
There it is. The component owner's workflow, and pretty much what Schwan suggested of, adding…
to the code owners, basically the asterisk, and then kind of our names. We'll just…
Take care of the assignees for every, or, you know, the review… the reviewers requested.
Ariel @arielvalentin (ATX, USA) 00:35:57 Right.
Kayla Reopelle 00:35:58 For everyone that doesn't have, like, a specific
component owner, and will also still be assigned to all of the ones that do have component owners. So I think that takes care of,
Some of the concerns we had about it.
Are there any other Yeah, sorry I cut you off.
Ariel @arielvalentin (ATX, USA) 00:36:16 So, I was gonna say, this is… is the component owners only triageers, or do maintainers and approvers end up in that list as well?
Like, for example, like, I… do a lot of work with the rack one, and the active job one.
So McKay being the co-owners of those, for example, and Trilogy.
Right? Do… do maintainers end up on those, or…
Kayla Reopelle 00:36:39 So, maintainers will still be… like, should we add maintainers to this list? I think…
Ariel @arielvalentin (ATX, USA) 00:36:44 Yeah, I was wondering if this was only.
Kayla Reopelle 00:36:46 for training.
Ariel @arielvalentin (ATX, USA) 00:36:46 triageers.
Kayla Reopelle 00:36:47 No, I think that it would be good to know who we can go to for any particular issue. So if a maintainer, yeah, feels…
like, they want to take on, you know, an individual library. Like Rob's already listed on the processor baggage,
Ariel @arielvalentin (ATX, USA) 00:37:03 Gotcha, gotcha, gotcha.
Kayla Reopelle 00:37:05 Yeah, but I think if we're…
Comfortable with this, and it's approved.
We could add that in a separate PR.
Ariel @arielvalentin (ATX, USA) 00:37:15 Yeah, I think so.
Kayla Reopelle 00:37:16 Okay, so I'll get main merged in, and then,
Because, like, yeah, I think, Hannah, I don't know if you're interested in maintaining any of the…
HTTP stuff that you've worked on, or being, like, listed as a component owner there, that's… that's a future thing we could look into.
But awesome. I am excited to hopefully get some more, component owner engagement on some of these.
Cool.
Alright, HTTP metrics… Okay, cool,
Nice, thanks, thanks for opening this. I think… This is our third… implementation,
But it would be really nice to get it out there, and just actually, like, pick one. So, thanks for bringing this up. Is there anything you wanted to talk about at Synchronous, Sean?
Xuan Cao 00:38:29 So, I know that that has this kind of a PR, but I think… That is, that's…
PR that utilize matrix.
It's pretty old, based on how many, how many changes, Definitely mattress. And then…
And I don't expect this one to be merged, because there's a lot of changes.
Especially involves 3 different, instrumentation. I'm not sure if that's a good way to…
To have the PR to modify 3 different institutions at one time.
I mean, maybe have a base first, and then less important, like, data HTTP at second, and then the most important base at Rack.
But I just want to get some, like, feedback and, ideas, so say you just check if this is, a good…
Or Porsche?
So… so my idea is to try not to attach the, the original, instrumentation code, so to… to…
You know, if something changes then.
The matrix stuff had to change as well, so…
Yeah, basically just, those ideas.
I'll put together and have some test cases running.
Kayla Reopelle 00:39:52 Cool.
Yeah, thanks, thanks for getting this conversation started again. I will, take a look at it this week.
And yeah, I think I agree, too, that,
Making, like, probably doing this incrementally, like, merging a change into base.
And then…
probably, like, adding, you know… I like the libraries you picked, NetHTTP and RAC, as separate PRs for follow-ups.
Then it's kind of easier to track the work.
But,
Yeah, but also, you know, they will all trigger their own releases, so maybe it's fine to do them… do them all at once anyway. I'll have to think about it more.
Does anyone else have, comments on this before we move forward? I only have 5 minutes left.
Ariel @arielvalentin (ATX, USA) 00:40:45 I wonder if this is forcing us to think about how the implementations are implemented?
And if we should have only one entry point per gam, And then, kind of.
Hogs in sort of, like.
And… I hate to use the word adapter API, but some sort of facade that
We're making calls into, and then…
The different elementary streams are getting added dynamically.
As opposed to, like, But I'm… but, you know…
That might make your runtime a little bit more complicated.
But what I mean by that is, we have sort of, like, the tracer and the leader.
And they're being… We have the implementation of Tracer and meter.
And then Zoom Logger. Like, as more teams are like, hey, get added to…
Kayla Reopelle 00:41:47 Right, yeah, that'll be…
Ariel @arielvalentin (ATX, USA) 00:41:48 profiler and whatever.
Kayla Reopelle 00:41:50 And, yeah.
Ariel @arielvalentin (ATX, USA) 00:41:51 And, I wonder if there should be some sort of composite API that's, like.
Go and do this thing, and… If you're collecting telemetry.
And then the composite object is iterating over all of the different
components that need an update, the only… I'm being naive here.
Obviously, because, you know, we have semantic conventions specifically around the HTTP-related things.
And then… If we, like, if we derive the metrics from the trace spans, but you can…
You know, have metrics without tracing, so…
Kayla Reopelle 00:42:40 Yeah, I feel like that's often handled
in the SDK, like, with the metrics enabled, disabled, I think that the dream there is that you'd be able to turn off the meter, and then the pipeline wouldn't really continue, so you'd turn off a meter for a particular instrumentation.
Ariel @arielvalentin (ATX, USA) 00:42:58 Yeah.
Kayla Reopelle 00:42:59 But… but maybe… maybe I'm not fully understanding what… what it is that you're proposing.
Ariel @arielvalentin (ATX, USA) 00:43:04 No, I guess it's like, we're looking at how the code is implemented, right? And we look at, say, 227.
So, anytime this code is executed, it's checking to see if the meter's been enabled at all, right?
Kayla Reopelle 00:43:17 I see, I see, yeah.
Ariel @arielvalentin (ATX, USA) 00:43:18 what I'm… but…
well, what… we don't want to do that check every time. I don't know if this is happening…
Kayla Reopelle 00:43:25 I think it'.
Ariel @arielvalentin (ATX, USA) 00:43:26 That's happening.
Kayla Reopelle 00:43:26 Initialization. Yeah, so it should only run once.
Ariel @arielvalentin (ATX, USA) 00:43:30 And it's like, that's happening…
No, I'm sorry, so then I guess we'd end up with a proxy wherever the…
the calls are being made. If we pick… let's look at the… Rack Event Handler 1.
Kayla Reopelle 00:43:47 Okay.
Ariel @arielvalentin (ATX, USA) 00:43:51 Okay, so in this case, Ron is doing a thing where he's adding more event handler… another event handler to the event handler list.
Which is kind of like… in my head, I'm thinking, oh yeah, we would have this…
chain of things, a composite, effectively, which is a list of event handlers that's like.
you add or remove whatever event handler, and you iterate over them, and there's… the configuration happens once at startup.
Kayla Reopelle 00:44:17 Yeah.
Ariel @arielvalentin (ATX, USA) 00:44:17 But we don't have that in, say, NetHTTP, where
You have the instrumentation metrics portion of it. Let's take a look at that one.
Because we're monkey patching, and it doesn't have any hooks.
Kayla Reopelle 00:44:30 Yeah, you add another pre-pinned.
If metrics is, is present.
Ariel @arielvalentin (ATX, USA) 00:44:39 Yeah, go ahead with the actual implementation there. Yeah, so…
We're patching the interface, so we're adding two prepend patches.
to the interface, and I don't know, maybe we only need to re-pend it once, and then that thing delegates to…
A composite, a list of Things that need to get generated.
But, but yeah, I'm being naive there, right? Because the implementations are so wildly different.
Because, you know, like, how it's capturing the start time and the end time.
Kayla Reopelle 00:45:18 Yeah.
Ariel @arielvalentin (ATX, USA) 00:45:19 For recording the metric, which is…
which we should be using POSIX for those, but… but, darn it.
This isn't easy, is it?
Kayla Reopelle 00:45:34 No, but,
I mean, I think the other thing we can keep in mind is that this is all still experimental, and so we can change the implementation, too, as time goes on.
If we have other.
Ariel @arielvalentin (ATX, USA) 00:45:49 Thank you. Yeah.
Kayla Reopelle 00:45:49 For how to get it out there.
This has been a request from customers of ours, too, so it would be nice, I think, to just start recording the metrics. But I do think that before we stabilize it, we should make sure that we're doing it in, like.
the most performant way, the way that feels, you know, the most secure, because this is a big step for adding a new signal to our instrumentations, which we haven't done yet. So far, it's just been a single trace to worry about, and I know that
you have experience dealing with systems that need really, really great performance, so I think that you have an in on
how to design this, in ways that, you know, maybe other people don't. So, I definitely want to talk about it more. I do have to stop sharing my screen. I can switch to my phone to keep chatting, but I have to drive off to an appointment. I know we still have
A few other things that we want to talk about.
Does anyone else want to start sharing? I mean, I'm happy to keep talking while I drive.
Ariel @arielvalentin (ATX, USA) 00:46:54 No, no problem, you can… Try not to crash into anything. Be careful.
Kayla Reopelle 00:46:58 I will be.
Ariel @arielvalentin (ATX, USA) 00:47:00 I think I mostly have just, like, some stuff for Hana and I to discuss.
Kayla Reopelle 00:47:04 Okay.
Ariel @arielvalentin (ATX, USA) 00:47:05 But let me just make sure that I don't have anything salacious on my screen before I share it, because I…
Kayla Reopelle 00:47:12 Thanks.
Ariel @arielvalentin (ATX, USA) 00:47:13 I am known to do salacious things.
Kayla Reopelle 00:47:18 Okay, I'll see you guys on mobile.
Ariel @arielvalentin (ATX, USA) 00:47:23 Let's click this.
Y'all are so patient, thank you.
match Just to clone here…
Hopefully, all I have is Chrome in front of y'all, and not all my other things.
Kayla Reopelle 00:47:42 Yep.
Ariel @arielvalentin (ATX, USA) 00:47:46 Okay, so that was the discussion about HTTP and metrics. We want some more feedback in there, some ideation, pretty cool stuff. Thank you, Schwab.
And I'm gonna bring it back to… I didn't write this one, but I wrote this one. So, if you wanna,
some things… one, it… I started with, like, I'm trying to do this…
I'm gonna meet all of the needs of the specification, all in one big PR, and I was like, oh man, that's not a good idea. Too many changes, not enough to concentrate on.
And, I think, out of this one, the first PR really is to satisfy a single goal.
Which is to say… I want for the HTTP unknown methods to be supported, because it's inconsistent right now.
What do I mean by that? What I mean is…
whenever you have a HTTP method, There's the support of…
It should be one of these values, you know, well-known values of GET, POST, or head.
And in the section here, where it's describing
you can have a list of known methods from this RFC and patch, as well as some of these
experimental ones.
I've left the experimental ones out.
But whenever you hit an unknown HTTP method.
you should set the HTTP method value to other.
And so that's what the scope of this PR was.
Is to hit that unknown other method.
There's other things that are specified in here. So, for example, you can extend it by adding additional…
support the environment variables, I'm intentionally skipping that.
I'm saying, no, I'm not gonna do that. Not in this PR, anyway.
And then there's also the method original value, which was introduced in the later CENCOM specification.
So, my first step here was to say, let's support the… other…
You see how, like, all of these implementations all have, like, a different set of…
I think, like, that's easy. I mean, this is, ETH on here.
Sorry, let me sign the right one to look at.
they used to say something like NA on particular values, as opposed to it saying other.
So I'm focusing on it trying to do what the spec says, with… Some degree of backward compatibility.
Right?
And there's some test cases here where it's, like, breaking encapsulation, so, you know, I'm not even…
I'm not too worried about some of those other changes.
But there were some cases, like the Faraday one, did not ever allow other, while others would write NA instead of using other.
So that's what the scope and the focus is of this PR.
Does that make sense?
Hannah Ramadan 00:51:24 Yeah, Arielle, that makes sense.
Thanks for working through that mess of duplicated files. It is a lot. The only thing, taking a look at this, that we weren't sure about.
is changing the span names for current instrumentations, with, I guess anything in the old semantic convention? What do you think about that? Because I was a little nervous about, like, it…
I mean, even though it probably shouldn't be, like, the span name HEVNA or whatever, changing it…
I mean, I think this isn't a, you know, we're not a stable gem yet, so maybe you could just, like, change this band name, but I just wasn't confident about…
That piece.
Ariel @arielvalentin (ATX, USA) 00:52:12 Specifically around the NA one, where it's saying, NA is not the right fan name, and it never should have been.
Because the old… old case was… in the older version of the spec, if I understand it correctly.
If it's NA, it should say… it should only be… the span name should be HTTP, with no suffix.
Or no value?
versus… like, let me see if I have another example of this.
So if we looked at that, like, one of the duplicated helpers would be…
Here's what the span name should have been.
which were HTTP followed by method.
And then the other case would always be plain old HTTP with nothing in it.
So, in a sense, that's fixing the broken implementation, or, like, the thing that didn't even meet the old specification, right?
And that was only done in the EZGEM and nowhere else.
So the easy gem didn't do the same thing as other gems did.
Does that make sense?
Hannah Ramadan 00:53:22 Right, okay. So…
Ariel @arielvalentin (ATX, USA) 00:53:24 Or ethon, sorry, not easy, it was Ethon.
When?
Yeah, sorry, please go ahead, I apologize.
Hannah Ramadan 00:53:34 Oh yeah, no, so, yeah, it is fixing something that probably should have never been there in the first place. It's changing a span name…
like… I mean, we are moving towards…
like, in February, knocking out all the, like, old, semantic convention names, like, should that be a part of…
this PR to, like, correct that old mis…
Like, span name, or just moving forward.
I guess my question is, like, do we need to update the old…
semantic conventions, even though they are…
Ariel @arielvalentin (ATX, USA) 00:54:15 Yeah, because I use them still, like, we're… when we hit February, GitHub's gonna be frozen, and we won't be upgrading anymore.
Until we can move on to the latest version of the spec.
Right now, we're tied to the pre-version of the spec, so that's why I'm trying to get some of these fixes out, because I can't upgrade any of our current gems, because after the old
Middleware was introduced, we had monkey patches that were trying to cover the case of other, instead of having fixed them upstream, unfortunately.
And there's… specifically around Fastly's Purge API.
So, that's why I was trying to get this fixed before… The upgrades rolled out.
But what you're saying is that this is not acceptable with changing the span names and only…
keeping the old spannings, even if they're wrong in this PR.
I can… I can do that.
Hannah Ramadan 00:55:14 Okay, I guess I'm not sure, like, I… I… sometimes I'm like…
It kind of, you know, it seems like a breaking kit change, but then again.
we can do that at any time. So, I guess I just wanted to call that out as something I, like, wasn't sure about, maybe if other people have opinions, but…
I mean…
Ariel @arielvalentin (ATX, USA) 00:55:33 The follow-up PR that I have is specifically around span naming and supporting the new The newer specification?
Just for the new… SEMCOM and the stable SEMCOM ones.
So it's like adding a URL template as a… as a…
As part of the span name.
And keeping the old conventions
Updating the old conventions to meet what the…
old conventions should have been, and, like, we missed interim fixes, if you know what I'm saying.
Hannah Ramadan 00:56:10 Yeah.
Ariel @arielvalentin (ATX, USA) 00:56:11 If you want me to leave the old conventions alone, no problem, I can leave them alone and only do the new ones.
So we could leave the NAs broken as they are.
And in this PR, I can leave it only for the stable conventions to do the updates.
Would that be acceptable?
I don't mean to put you on the spot, you can think about it, you can say, let me get back to you.
Hannah Ramadan 00:56:39 Yeah, let me think about that. I don't know if… I mean, it's hard to hear
That they're currently broken, and that does seem like something…
that would be, like, worth fixing. So let me… let me think about that.
Ariel @arielvalentin (ATX, USA) 00:56:58 And then, if there's no further questions about that, because I've taken up too much of your time.
Juan is looking for feedback on runtime metrics for SUMCOM.
Is there anything specific that you'd like for… to share with us?
Xuan Cao 00:57:16 No, not really, just, I, there's… there's more metrics that we can record, but this is something I think is…
Kinda important, and also,
maybe, similar to what, Python, say Python, the Node.js has, mostly just the,
the coverage collector status.
And, other… some of the, like, those, like, those persons time, like, old person's core, actually, they're very important, but I'm just trying to get an idea to… to make the… the most,
importance and the compact of the runtime matrix, but now I can't,
open PR to add those stuff.
Ariel @arielvalentin (ATX, USA) 00:58:04 Gotcha, so you're looking from engagement from us, and looking in the SIG here?
To make sure, oh, naming matches, and, you know.
Xuan Cao 00:58:13 Yeah.
Ariel @arielvalentin (ATX, USA) 00:58:14 It's symmetric with what you would see in other SIGs.
Yeah, makes sense.
Xuan Cao 00:58:19 Yeah, yeah, yeah, that's not… that kind of sense, yeah.
Ariel @arielvalentin (ATX, USA) 00:58:22 Do you know if there's, like, a… If there's, like, a group,
Like, a working group for these, or is it just a… The specs are, pretty much.
Xuan Cao 00:58:37 Oh… There's going to be missing?
Ariel @arielvalentin (ATX, USA) 00:58:40 I gotta move.
Xuan Cao 00:58:43 I think it's for the specific.
Ariel @arielvalentin (ATX, USA) 00:58:58 Okay.
Are there other… what does New Relic do for these, Hana?
Are there anything… is there anybody who worked on the agent that worked on…
like, Ruby metrics, that would, you know, runtime metrics, that would be interesting.
For them to collaborate?
Hannah Ramadan 00:59:16 We don't currently collect runtime metrics like the ones listed, I think.
Ariel @arielvalentin (ATX, USA) 00:59:21 Mmm.
Hannah Ramadan 00:59:22 we've… we have discussion about it. I think it maybe might have to do more so with the UI, not knowing what to do with these quite yet.
Ariel @arielvalentin (ATX, USA) 00:59:31 Gotcha. What about you, Alex? Heroku got anything interesting?
Around that.
Alex Arnell 00:59:38 Mmm… a lot of what we…
I've been collecting is kind of, like, internal…
We don't… yeah, we're migrating toward using OTEL to collect these things, so it's… it's on the radar, hence why I'm here.
But yeah, and most of us, I think most of what we collect would be, in the language, our language field pack stuff. I can't… I don't remember the specifics.
I think, though, from what I recall, so we have…
recently tried to update the semantic conventions for the signals that Heroku emits as part of our new platform.
And I think there's, like, a new process there where you kind of stand up a standalone SIG for it to discuss things. We kind of…
Got that feedback.
yeah, it was kind of like, we submitted the PR,
And it was, like, looked like it was gonna go through, and then…
The process has changed, so we're kind of figuring that out.
Ariel @arielvalentin (ATX, USA) 01:01:02 Wait, they, they wanna… set up a SIG just for Heroku, STEM comp?
Alex Arnell 01:01:09 Yep.
Ariel @arielvalentin (ATX, USA) 01:01:10 Interesting.
Sounds to me like you could just publish yours.
On your website, and then just be like.
This is what you get from the resource attributes!
Alex Arnell 01:01:22 Like, yeah, that's what we've done, basically. So, now we just wanted to make sure that the semantic conventions matched.
But, yeah.
Ariel @arielvalentin (ATX, USA) 01:01:31 Okay.
Alright, as an end user of this stuff, like, any thoughts, concerns, or…
Alex Arnell 01:01:44 No, these… this stuff would all be fantastic.
Ariel @arielvalentin (ATX, USA) 01:01:46 Okay.
So, you know, as… from the perspective of your… of your users.
you know, it would be great to see some feedback in something like this, because they… these metrics would be useful for Heroku.
for Heroku to be able to display for the user, or whatever your…
You know, guidance for your users to say, this is what's available if you attach
a collector, or whatever it is, however it is that these metrics would get collected.
It'd be great to get some feedback from you all about that.
Alex Arnell 01:02:19 Yep I'd be happy to.
Ariel @arielvalentin (ATX, USA) 01:02:22 Thank you so much.
Shawan, is there anything else on your mind about that one?
Xuan Cao 01:02:34 Nope.
Ariel @arielvalentin (ATX, USA) 01:02:36 Okay. Well, we are over on time by 2 minutes, so I want to say thank you, everybody, for tolerating me yet again.
And, the only other thing was the same blog post that Kayla had mentioned. I wanted to talk about it more, but maybe we talk about that in the next one. So…
Thank you very much, everybody, for your collaboration.
And we'll chat next time.
Xuan Cao 01:03:00 Thanks, thank you.
Hannah Ramadan 01:03:01 Awesome, see you guys.
