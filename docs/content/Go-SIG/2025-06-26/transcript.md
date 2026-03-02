SIG: Go SIG
Date: 2025-06-26
Duration: 49 minutes
Zoom Recording URL: https://zoom.us/rec/share/8gQzWUL-2ZJrGVqffrr6-ADScJYRner4gy-uvBXFgzd6iM_YitYVuF3ACc79OuNX.5Amq4cEjv2CJxV4Z
============================================================

## Zoom Recording Transcript

**Robert Pająk** 00:20 Hello, Tyler! Hello, Sam.
**Tyler Yahn** 00:23 How's it going.
**Sam** 00:24 Hello!
**Robert Pająk** 00:28 So he's going.
I might need to eat something in 10 min, or just shut down the camera and mute myself. I just don't want to fight
so sorry for being rude, but you will not see it.
**Tyler Yahn** 01:00 No worries.
It's dinnertime there, right.
**Robert Pająk** 01:04 Actually like dinner, like, you know, the late like 6 pm. Usually we are eating dinner like 2 pm. In Poland, one Pm.
**Tyler Yahn** 01:12 Oh!
**Robert Pająk** 01:12 But.
**Tyler Yahn** 01:13 Okay.
**Robert Pająk** 01:13 I didn't have time today today.
**Tyler Yahn** 01:21 Yeah, nice?
Well, yeah, we could probably get started then. I see David's on as well. Yeah, if you haven't yet
added your name to the attendees list. Please go ahead and do so.
If you have agenda items you want to talk about.
go ahead and add them as well.
and I'll start sharing my screen here.
Yeah, sometimes when you upgrade. Zoom, it just really is a bad idea.
anyways. Okay, so starts off Robert. There's a new team for code owners, go contributors that you want to talk about.
**Robert Pająk** 02:03 I think it's just a heads up. I think that
probably trust or someone else made some changes in the organization.
And basically the code owner. It was, I think it was not that this automation that was adding our code owners to the review stopped working.
and, as far as I understood, the workaround was just to add a new team. So that basically, these people are part of the, you know, repository, etcetera. So basically, what was done. There is a separate team called Go Contributors, which is, I think, the parent is 3 azures.
our triagers, but it's a separate team, so we do not say that they are responsible for triaging. It's only for sake of for basically our automation that it works.
If anyone opposes and think that it was a bad idea. Then just pick out
here. You see, this contributors here.
So here we have basically, I think it consists of
maintainers, approvers, triagers, and code owners. Right now.
**Tyler Yahn** 03:20 Hmm, okay.
Oh, okay, this is the code owners as well. Okay.
what? I don't. What's the downside here of having another team like, does this team have permissions or repositories? It doesn't look like it doesn't need repositories.
**Robert Pająk** 03:36 I think it has triage. It has only triage role. It would be different later if you would like to change it. But.
**Tyler Yahn** 03:44 And then.
**Robert Pająk** 03:44 Together with Damien, we found that triage is a good way. Because people can, you know, set labels, close issues, reopen issues. So we find that it's okay for a code owner to have triage permissions.
They do not have right, which is most important, so they cannot create tags or branches, etc. Which is the most critical. I think responsibility.
And the only downside is that in theory, anyone from the organization can just tag every code owner. And I think that Yuri was not in favor of this, but he didn't. He didn't speak up to when this idea was brought up, so I'm not sure.
**David Ashpole** 04:27 Will it only tag code owners, or will it tag everyone with all the features.
**Robert Pająk** 04:33 Everyone who's here.
**Tyler Yahn** 04:36 Wait. So if it requests a review, does it request.
**Robert Pająk** 04:39 No, no, no, no, if some.
Okay, please.
Italy.
Yeah, it's right.
**Tyler Yahn** 04:43 No just text. Me.
**Robert Pająk** 04:45 Yeah, the automation is the same.
**Tyler Yahn** 04:47 Okay.
**David Ashpole** 04:47 I see, but we don't use that, alias right.
**Robert Pająk** 04:51 No.
**David Ashpole** 04:52 Triage. Everyone. Okay.
I think that.
**Robert Pająk** 04:56 That's yes, and for me.
The next item is about recording Earth exceptions.
and maybe I'll share my screen, Tyler, because I have opened some tabs.
**Tyler Yahn** 05:11 Yeah.
**Robert Pająk** 05:14 I will see how shingles will work for me today.
Okay, this is not this one, not this one.
Okay, so this, basically.
So it will be a little bit summary of my understanding.
So the issue was about basically was about using span record error for auto Http, and it I do not remember if it was Damir's or some Pr basically to change a little bit, the behavior.
And basically I started looking at the semantic convention specification, Doc, etc.
How basically, we should react on errors
and the things which I was trying to understand. Here I was also double checking with Trask and Ludomiwa, or semantic convention maintainers. And basically I wanted to double check them with them. And basically they confirmed everything everything that I understand here. So
basically, there are a little bit of unclarity in the semantic conventions, but they agreed that basically this is more like of things that needs to be just more well documented and not my, and that my understanding is pretty correct.
So basically, initially, there was an Oh, oh, shoot, because I have to click something here.
Okay, so initially the trace exceptions. There was a recording exception in the trace Api.
and this is like stable.
but later they created as part of the semantic confession. A separate contact concept called an error.
And basically an exception is being is basically something like an a handled exception.
So from our goal perspective, it's basically a panic.
And when we are, I was showing all the examples that I was aware of, they kind of agreed that basically this kind of thing recording exception. The thing which is here is basically about unhandled exception.
handling basically and
regarding errors. So if there's some Api which simply returns a there, that, for example, you make a request which, for example, failed. Is this so we, this could be. They see it like as a
terminating error. So you know you have an in the library that reports a status that basically something failed. But it's a not an exception, just a regular, you know, failing stuff. Then we have this recording error in the semantic conventions.
And basically
what it says is that when we record these errors, you just have a separate error type attribute. Previously it was exception, type attribute. You should set the status to error because basically, something has failed.
and you use the description, etc.
And you do not need to emit this span events, etc. Basically, you know, you have a span. It failed, you know. It stopped. It failed. There's no need to add any additional span events. It's a redundant information.
So this is the second thing.
and the thing which is also missing currently semantic. So I was checking how we are handling this kind of stuff. So we are using this record error in, probably. So I thought about just calling this span error and making basically, the implementation is kind of compliant of this development semantic convention. So one of the problems is that we do not have nice handling for this error type.
Right now, I think some. This is like kind of internal copy, paste it in some places.
So I was thinking about putting something semantic conventions around that
the other problem which I also discovered
is that everywhere in the recording exceptions here.
it's basically all of the examples are saying, if there's an exception set status to error here.
And even here it's also kind of saying set status to error, which is an example. The problem is that the specification doesn't say that when there's an exception, the
the span should be set to error, there is nothing
saying it explicitly using the normative language, and basically both tries to the mua said that it is, in their opinion, back in the specification, because if there's an exception, then something is basically terribly wrong. And they said that probably when we had this
code here, which is about this one which is basically
on span, and we are recovering. If there was a panic which was not handled.
Then they said that we should. We should be fine. We should also set the span status to error here.
because right now, if there's a panic.
We are just bubbling up. We are panicking again. But the span status is still unset.
and they think that it is a basically a back end specification that it was not called out.
so I will probably work on the semantic adventure specification to propose and fix it. I do not want to change this code and set this status to error before we have a confirmation from the specification box. And I also thought about, basically, I created 3 issues, I think, which are kind of
separate issues.
Sorry.
**Tyler Yahn** 11:15 So that span status thing was intentional. By the way.
like that was something that was discussed.
People talked about that, and they didn't want to override any user set value there.
**Robert Pająk** 11:29 You mean that if some am I sharing right now or not? Or have I.
**Tyler Yahn** 11:34 You are.
**Robert Pająk** 11:35 Again.
**Tyler Yahn** 11:35 We're looking at a comment of yours that says Tbh. I am not sure.
**Robert Pająk** 11:40 Okay, my zoom making you crazy.
**Tyler Yahn** 11:46 Welcome to the club. All right. This is not just me. Yeah, but
no like. So this is something that people were concerned about like
this is a part of the discussion for the set set status, especially in regard to this record error, like, if the status is like already been set, or it's been unset by somebody overriding it. With this exception, was contradictory to what their intention was.
and since it's already determine that you can look at the
you can look in an event to record an error. It was it was. That was why it was omitted from the specification.
Whether we want to change that or not I don't know. I mean, we're obviously changing things like this. Record error path was is new as well.
This was also something that was discussed like there used to be a doc in here also that said, like, you know, go. Errors are exceptions. So they're they're recorded as exceptions. So like.
**Robert Pająk** 12:39 Said in this document which I was sharing, and I.
**Tyler Yahn** 12:42 It's it was set somewhere. I thought it was in this document. But I haven't. Yeah. I I'd have to go look
**Robert Pająk** 12:47 Okay.
**Tyler Yahn** 12:49 There is. There was a whole.
It might have been somewhere, some issue. Go ahead.
**Sam** 12:55 But I feel good. Errors are exceptions, and usually panic won't happen.
So if we don't record as well, exception that there is no arrow could mark into spam, never.
**Tyler Yahn** 13:14 So I mean, I'm not. I'm not opposed to
different error recording paths like that's that's not I. Just.
I think that it needs to be careful about, like the original conversation around, like the set status like that was, I agree, like, I think, that we need to have some clarification from the specification level on whether you should be setting it or not, and it should be defined because I I would not want to change our implementation based on my understanding of history like that was.
**Robert Pająk** 13:42 Yes.
**Tyler Yahn** 13:43 And if specification wants to change that and put it into some sort of codified language that sounds good to me. But.
**Robert Pająk** 13:49 Yeah, that's my intention. Try to basically
make it more clear on the specification side, and just make some draft Prs to make it also more like visible what you know just kind of like a prototype.
**Tyler Yahn** 14:02 Yeah, because I mean, I do think.
**Robert Pająk** 14:04 No forms. But I really do not like the current state of, you know. Exceptions. Error, Spanix, how it is being documented, because I saw that it's confusing for many languages.
**Tyler Yahn** 14:15 Well, I mean the place that you referenced also in the SDK is not the only place that record error is used right
like there's a lot of other places that that's used and that's using the same semantics.
So I mean, I don't know. I
it is a change in the behavior of the specification of this new development thing. So like, that's
yeah, I think we should take a look at it now before it solidifies is also a good idea like you're.
**Robert Pająk** 14:41 Okay.
**Tyler Yahn** 14:42 Yeah.
**Robert Pająk** 14:48 So that's all from my part, so
I will try to work on it. But probably, like I won't start sooner than in 2 weeks, because I want also to finish other stuff.
**Tyler Yahn** 15:01 Yeah. No worries.
**Robert Pająk** 15:02 But it's on my radar. It's on my radar.
**Tyler Yahn** 15:08 Okay, cool.
All right. Last thing on the agenda is something that came up in the specification meeting this past Tuesday was the declarative configuration is trying to go stable, which is in this Pr. Here. One of the things that Robert pointed out in the meeting is that a lot of the times, like
the specification, would go stable. And then we come along
and we find a bunch of things. And so the goal was to try to not have that happen or try to minimize the that that chance. Luckily we have an implementation of
of this declarative configuration like package in Contrib.
It's been reviewed by people who are already involved in the specification for declarative config, or are just not really paying attention, or I don't know how to say that, but like at the end of the day, like the question was asked like, Can we do an audit of that? And can we do an audit of that by maybe somebody who's not as familiar so that they can, you know, learn about the specification and read it with clean eyes, so that it doesn't. You know they don't come into it with any bias of like context and understanding that
you know anyone in the Sig would know about
is kind of the ask.
So I guess what I'm looking for is a volunteer here who isn't a part of the declarative config working group or working group to review our implementation in the contrib repo
and asking for volunteers. The thing is is that we needed it. Need it probably pretty soon. By that I mean an audit done within a week. It shouldn't be nearly as complex of an audit as we've done in the past. Probably. Actually, I think there's a v. 4 in here, too.
**David Ashpole** 16:49 What makes you do that.
**Tyler Yahn** 16:51 It's much smaller in scope of specification.
Yeah, it's
So the actual like, schema itself
is like, that's that's 1 thing. But the actual like. You know, Api and SDK like these are the things that I think that need to be audited, because these are the things that are being proposed to go stable here, which is.
you know, much, much simpler. One of the things that is like kind of interesting is like the extension, for like instrumentation, I think, is also interesting. So we need to make sure, like we can support that. I think that's probably the the most complex part of this.
But yeah, it's really these these 2 documents. And I'm happy to create issues to do this audit there, I just didn't. Yeah, I can create issues. And I can definitely like Link to a lot of different things.
I just want to know if there's anybody here who can do that.
**David Ashpole** 17:52 I can do that.
**Tyler Yahn** 17:53 Okay.
**David Ashpole** 17:54 How do we do them.
**Tyler Yahn** 17:56 Awesome. Yeah. So would it help if I create you some issues for that, and then link them or assign them to you?
**David Ashpole** 18:03 Yep, please do. And yeah, make sure it talks about whether it's just the Api and SDK, or whether I'm also supposed to look at.
You know the config surface itself.
**Tyler Yahn** 18:15 Yeah, it's.
**Robert Pająk** 18:19 Kind of they're coupled to each other, I will say in some way, same places.
**Tyler Yahn** 18:25 They are. But I also think that there's like, yeah, like, I mean, here's another thing like this isn't even going stable. I'll look more into like what actually needs to get audited.
The thing is is, though, it's like
there's already like a set of unit tests in there.
Yeah, I'll look into it. I'll create some issues for you. If it's too much of a burden, then we can also split it up within the next next week.
**David Ashpole** 18:53 If it's just like like this is easy bread and butter, stuff like new configurator, or whatever.
**Robert Pająk** 19:02 So there is one place which I am concerned about
the Plugin, the Plugin stuff, and the plugin, how it is being documented right now like this is also connected with this config properties. Basically, how parse I think there are.
because, if I remember correctly, the SDK for the configuration talks about
2 things, 2 methods. One is parse, and second is create.
**Tyler Yahn** 19:32 You.
**Robert Pająk** 19:32 Yeah.
And basically, I do not see
how the I would say that it is very
The thing is that it is kind of strangely, in my opinion, defined how Parse works for the plugins
given. It represents something like, I will say. Jason put everything.
but at the other side it also mentions, for example, Java Spi, which is kind of a Java mechanism to support like reflection, creating by creating by reflection, which means that it will be something a little bit different than, in my opinion, this model, I think there are separate config structures, and not the things which is defined in the in the specification. This is kind of my understanding. Maybe I'm wrong. But I think that this is kind of basically
someone tried to basically set in the specification you could put anything but at the safety. There is a this kind of model put.
and I'm not really sure how to understand it, because, as far as I understand, the idea is that
you should be able to put
any custom processor exporter that you could then reuse. For instance, you know I would like to have the Mini minimum severity processor
to be able to be put in the config somehow, so that you can, you know, wrap, for example, and put one processor into the second one. I think this should be possible to support it. Do you follow me, Tyler, or not? Really, because I know that I okay.
**Tyler Yahn** 21:20 It should be. It's just like.
**Robert Pająk** 21:22 For example, said to me or Jack, No, it's not possible, and I think it should be possible. So.
**Tyler Yahn** 21:31 Hmm!
**David Ashpole** 21:32 Is this that we don't like the design, or that our implementation isn't like? Is this like.
**Robert Pająk** 21:41 Now we publish is doing nothing with this. If you have to check properly.
**Tyler Yahn** 21:46 That. Yeah, that is true. Like, I don't think that we're actually doing extensions beyond the Standard Standard Library. But like.
I hmm.
I don't know we'd we'd thought through this. I thought there was a prototype as well that Alex had that dealt with something like this as well. I can go take another look.
because the idea.
**Robert Pająk** 22:07 My only this is my main concern, basically, Tyler. Only this Plugin mechanisms, how it will work
no other than that, if I remember correctly.
**Tyler Yahn** 22:15 Maybe I.
**David Ashpole** 22:16 Even.
**Tyler Yahn** 22:17 Yeah, we we can do that, too. Yeah.
we had talked about. It is the same way that we do like the auto export and the auto prop stuff right where there's some sort of registration mechanism.
So any sort of processor or anything that can be named essentially within that chain, we could support it in that sense. Yes, but the.
**Robert Pająk** 22:35 Is, that is only a name. You cannot put any more parameters.
or the auto prop, etc.
**Tyler Yahn** 22:42 You cannot put, you know.
No, that shouldn't be the case, like the when you register. Whatever the auto prop is, you also need to register some sort of like parsing agent of of configuration, right?
So like the.
**Robert Pająk** 22:57 Yes, this is my idea as well. In the same way.
**Tyler Yahn** 23:02 Yeah, that was, that was the original intention. Was that like it, it not only is like the the component, but it also is like the you know the setup? Yeah, yeah, exactly. Yeah.
So, and so that was.
**David Ashpole** 23:16 If I can interrupt, it sounds like this is not implemented today, right? This part of the spec.
**Tyler Yahn** 23:20 No, but I don't think
sorry. Go ahead. I keep cutting you off.
**David Ashpole** 23:27 I cut you off first.st
like this is not implemented in the spec today, right? Or in our implementation today. And we're trying to assess feasibility. Is that the goal.
**Tyler Yahn** 23:40 Yeah. But yeah, and this is, I think this is the, I think this is why this is still marked as development, though this config provider.
**David Ashpole** 23:47 So this is not going stable. This configuration.
**Tyler Yahn** 23:51 Correct. Yeah.
**David Ashpole** 23:53 Then
wait. So what is Jack proposing to mark stable cause? That's the stuff I want to make sure we get the audit done on and get our feedback. If it's just like a development thing, then like that is, it is good for us to give feedback on it. But it's not like. That's not the urgent part today, right?
**Tyler Yahn** 24:09 So so this config provider is the thing that like is
allows the extensions as well, though so this is the thing that comes behind the Api. So the the Api should. Still, the thing that's going stable is essentially like the core. SDK,
so you should be able to set up and create an SDK from a configuration file without instrumentation. Extensions without additional processors, or something like that like this, should be like something that you should be able to do, and that's the stable part.
**Robert Pająk** 24:38 So, Taylor, I got a different impression when Jack was express, describing into respect meeting. I think he was saying that Plugins and custom processors are still important, that the unknown is the instrumentation config, which is something separate to, you know, provider set. As to logger, provider, meter, provider, and logger meter and trace provider. This is how I understood it during the specifications
that basically the config provider was meant to be something, you know, like a 4th pillar, like, you know, a property back, basically for instrumentations and or other custom stuff.
**Tyler Yahn** 25:22 Yeah, I don't know about other custom stuff like, I think
other custom stuff includes like extensions. Like includes additional processors, includes
all of these other things. That's my understanding of this. I'm not exactly sure how I follow. It isn't.
**Robert Pająk** 25:40 So I think that what Jack said that he didn't. He thought that
this is critical to have support for this custom processors, etc. So maybe it might be good.
**Tyler Yahn** 25:51 Let me double check.
It is critical like that's definitely, but I don't think it's included in the scope of stabilization is is the thing, though.
**Robert Pająk** 25:59 So it will need to be double checked.
**Tyler Yahn** 26:03 Well, I mean I'm I'm looking at it right now.
I don't.
**Robert Pająk** 26:09 Yes, but when you have this config provider, then
does it mean that the processors will be also here?
Or it should be, for example, in the logger provider. Somehow.
**Tyler Yahn** 26:24 In the logger provider like in.
**Robert Pająk** 26:25 I mean how I do not understand
how you would add the capability to for for the plugins later.
So if you want to create. If I understood the design correctly.
if you have the, if you have, for instance, the Parse method, if you want to create a tracer provider.
you may want to pass on the
the logger provider. You do. I'm not sure if you want to pass also the logger, the config provider like. Do you need to pass all of the 4 providers to set up the SDK, or do you want to have, you know, kind of be possible to
decouple it and work separately that the that. So that's something not clear from the specification. In my opinion.
But maybe I do not really.
**Tyler Yahn** 27:31 So. So your your question is is like, at the end of the day, like
I've got a I've got a config file. That config file has, like a min severity, parser like defined like, how does that translate into a logger provider with the mins? Severity processor being used right.
**Robert Pająk** 27:47 Yep. Yep.
**Tyler Yahn** 27:49 Yes, I don't. I don't think that's supported today. And what we have. And so what you're saying is is like, how does that look going forward and like, is there a stability thing going to get in the way of that.
**Robert Pająk** 27:59 Yep.
**Tyler Yahn** 28:01 Yeah, so I don't. I always saw that like there was a an extension like a registration like config provider that was going to be added.
and that would have maybe a like it would. It would essentially load the
the correct things within whatever is returned for this logger provider
and that logger provider could then, you know, parse things appropriately. But I could
maybe take a step back and take a look at it before
yeah, I mean, I could take another look. But I think that was always the design goal was to
okay, have extensions supported there.
I mean, I can think through it again. I thought Alex also had a Pr for this. So all right, I can take another look.
**Robert Pająk** 28:47 Yeah, we can double check. I can double check also. Later. I might have you know. Apparently I might miss something. You know, I just may not connect it to dots each other correctly.
**Tyler Yahn** 28:59 Yeah, I mean, I just wanna be careful here. So that makes sense.
**David Ashpole** 29:02 Some dumb question, but it looked like config. Provider was not being marked stable.
**Tyler Yahn** 29:08 Right.
**David Ashpole** 29:12 What does it mean to stabilize
the rest of it without config? Is config provider, not like tracer provider, or something where it's like the
fundamental unit of.
**Tyler Yahn** 29:24 I think it's the SDK implementation of the the Api, though, is, is not stabilized right? So I think that's where this is coming in.
**David Ashpole** 29:31 Okay? So the the Api is going stable.
But the SDK implementation of config provider isn't.
**Tyler Yahn** 29:40 Yeah, that's how I've read this. Yes.
**David Ashpole** 29:42 Okay. Okay.
Okay.
Good.
**Tyler Yahn** 29:51 Yeah, I mean, I let's see.
I guess I'm also configuration data model. I guess it's only the data model. I guess I'm not actually seeing the Api being pulled out here. Maybe I'll ask.
Hmm.
yeah, that's actually a good question.
I feel like there's some this is not reflective of what the conversation we had at the Sig meeting was. I thought there was supposed to be at a different change here. But okay,
I could take, I could take a closer look. I I
don't think this is maybe ready for handing off to other people in the Sig. Then, if that's the case.
But yeah, I'll I'll ping you.
**David Ashpole** 30:36 I hope, or whatever.
**Tyler Yahn** 30:39 Sorry go ahead.
**David Ashpole** 30:40 I can still start on the Api audit, if that's like clear.
**Tyler Yahn** 30:48 Yeah, I think I mean, I think any new eyes going in and looking at this may be helpful, especially even just asking questions. And like, if things aren't making sense.
I don't want to make issues and assign them to you, though, until I'm sure that, like
it actually does make sense. So. But yeah, I think we can. We can take a look, though.
**Robert Pająk** 31:07 I have a question, what is the sense?
Where will be the Api implemented? Why do we have the distinction between Api and SDK?
**Tyler Yahn** 31:20 In, the.
**Robert Pająk** 31:21 I will say why I'm asking. I'm asking, because I have a feeling that the configuration, you know all this configuration model
is tightly coupled to the sdks.
You know it has this processors and stuff like that which is not which are not concepts of the Api. What actual open telemetry SDK implementation.
**Tyler Yahn** 31:43 Well, I think that's intentional. I don't think that that was ever meant to not be the case, like I think they are supposed to be tightly coupled like this, configuration is configuration for an SDK,
yeah, it's just that like, what's that Api look like? And then what backs that? Api is is the parlance of open telemetry is is what's being said here
like, I mean, it's kind of the same thing with like our SDK like there's an Api to our SDK, if that makes sense.
and it's not the open telemetry. Api is what I'm talking about like. There's like a code concept of the Api versus like the signal Api.
**Robert Pająk** 32:18 So this is the same concept or different concept, like the signal Api.
**Tyler Yahn** 32:23 No, it's not the same as a signal. I mean.
they're coupled to the signal. But no, it's it's more of a coding concept of an Api here.
**Robert Pająk** 32:31 So we do not need to have separate packages for the Api and SDK, the SDK will be just an okay. Because that was I, what? I was worried. So basically, the Api just represent the user facing Api and the SDK just represents the implementation. But is it correct?
Yeah, I understand. Okay, yeah.
**David Ashpole** 32:51 It's confusing as heck. Yes.
**Robert Pająk** 32:53 It's it's confusing as hell. If it will be codified like this in the specific issue. I would rather say there's a configuration component. This is the public Api. This is the internals, because otherwise.
**Tyler Yahn** 33:06 I think that's fair. I think we could. We could probably make that clearer. Yeah.
But yeah, no, there was never an intention to have this be like a generic configuration like signal essentially like that was never. No.
it's always been intended to configure open telemetry. Yeah.
**Robert Pająk** 33:23 On the other hand, I see a use case when you have instrumentation libraries
which may want to have some kind of
property back. I don't know. But maybe it's a separate interface, and maybe just the config implementation can. Just, you know, honor this interface. So I don't think it's I think it's still future, compliant, future compatible.
**Tyler Yahn** 33:47 Yeah, that is a that is a that is an open question. Yeah, that that's definitely how. How is this extended instrumentation is interesting.
**Robert Pająk** 33:56 But I don't see as a blocker, I think simply. If you have the configuration model which is being parsed and you have it, you can just, you know, give some get or whatever, and pass it to some other Api.
**Tyler Yahn** 34:10 Right? Correct. Yeah. And that's how it was designed.
Well, in theory, like the actual, like, Java's worked a lot more with, like, actually implementing what you just talked about. So there is a steel thread there and go. I don't think there's 1 for instrumentation like there's 1 for like ideas for components. But like, we always thought that if you can use this component like pathway, you should be able to do the similar thing for instrumentation as well. So yeah.
**Sam** 34:34 But I wonder if there is a 3rd party SDK implementation, how it's going to be
like affect the configuration part.
**Tyler Yahn** 34:44 It's it's kind of like what we were just talking about, though, like.
so if you have a 3rd party instrumentation library and you want configuration. You need to some way to like. Tell this library how to parse your configuration, and then get that from whatever this Api is.
**David Ashpole** 35:00 Sorry. The is the suggestion that this Configuration library should be able to initialize 3rd party sdks.
**Tyler Yahn** 35:11 I think this.
Maybe you can say it that way. I'd probably say it's more you should be able to add a hook for 3rd party instrumentation libraries
to receive configuration values for it like I don't know about initialize. I think I think that's still left up to the Instrumentation library itself.
But, like, if
if a user passes a configuration file and that configuration file is unified like into like one form, you should be able to like as an instrumentation library, expect, like the part that is relevant to you, to be passed to you.
**David Ashpole** 35:46 Interesting. So this you're saying, this isn't just for configuring opentelemetry sdks. This is also for configuring instrumentation.
**Tyler Yahn** 35:57 Currently. No. But yes, that's the the long-term vision. Correct? Yeah.
currently, that that functionality doesn't exist. But like in theory, yes, I mean in in Java. They are working on this like they actually have prototypes for a lot of this stuff.
But yes, that's that's the goal.
**Robert Pająk** 36:16 So in theory this package will be that
it will be almost as important as an Api package. Right.
**David Ashpole** 36:25 I don't know if I agree with that direction. I feel like this is why like views and samplers and stuff exist is because.
like the instrumentation shouldn't need to change.
It's just that.
**Tyler Yahn** 36:36 But so let's say you want to opt into semantic conventions.
**David Ashpole** 36:43 Like you want to use feature flags essentially.
**Tyler Yahn** 36:46 Yeah, or or, yeah, exactly like.
**David Ashpole** 36:49 Cream.
**Tyler Yahn** 36:49 Yeah, it.
**David Ashpole** 36:52 But you guys think.
**Tyler Yahn** 36:53 You can do environment variables right? But this whole point is to replace that with some sort of like static configuration.
And so that that's that's more what this is intended for. I mean, obviously, there's way more complex, like configuration you could have for instrumentation.
**David Ashpole** 37:08 I mean, like I would be happy if they added a notion of feature flags to the SDK.
As like a separately provided thing like propagators.
you know, get this like global feature flags. But.
**Tyler Yahn** 37:22 Well, yeah, I mean, I'm coming up with feature. Flex is the easiest of the comprehend. I don't think I have a really great example. But I mean there's there's nothing saying that you could have instrumentation that also needs more complex, like structured configuration as well like. If you know, you say you wanted
like, I guess a good example is like an auto instrumentation, right for Ebpf stuff in Obi, right?
If we wanted to pass in like right now, like there's already work being done on like, what? How do you like
configure this to have different
like levels of sampling for different, like, you know libraries or something like that, like you can have these complex samplers right? And like, you can probably do that in the SDK for, like
your own sampler, but, like it may also be like Ob provides configuration for this already natively. So why couldn't you just pass that configuration to the ob instrumentation? Right?
And that's that's definitely not going to be feature flag based. That's that's gonna be way more complex than that.
**David Ashpole** 38:22 Right like. What if I wanted to configure the with public endpoint on my Http thing right.
**Tyler Yahn** 38:31 Yeah, and like. And what if you wanted to like, do more than that? What if you wanted to like? Only allow a subset to be public endpoints, and the other, you know, are internal, so.
**David Ashpole** 38:40 Public endpoint, function.
**Tyler Yahn** 38:42 Yeah, exactly right. Yeah. Yeah. And so like, that kind of configuration is is.
I mean, maybe you could try to like shoehorn that into a feature flag. Actually, I guess. But I think that the intention here is to go to say like, instead of having just boolean values, or like static values like have more structure in the configuration that you pass through an instrumentation to support that in the long term. Yeah.
**David Ashpole** 39:08 I'll have to think about it.
I'm still.
**Tyler Yahn** 39:10 Yeah.
**David Ashpole** 39:11 Little unsure.
It feels like we've gone through a lot of work to try and put
end user configuration in the SDK and make it so that you write instrumentation once, and then you don't have to touch it, because a lot of times like
auto instrumentation is one thing, and Ebpf, sure, but a lot of times like instrumentation is buried within 6 libraries.
you know, and you can't pass stuff to it. So it gets.
**Tyler Yahn** 39:37 You know.
**David Ashpole** 39:39 It gets weird.
**Tyler Yahn** 39:41 I think I think it becomes more relevant for things like the collector, which is where this is being used right where they have, like native host instrumentation or networking instrumentation. That's also coupled in there.
But yeah, I know what you mean like. I also agree like to be clear, though, that that's why this is not included in the the first.st
**David Ashpole** 39:59 Sure, sure.
**Tyler Yahn** 40:00 Because, like your, your concerns are not unique.
People have also voiced these as being skeptical. So like, I think it like, we don't want it to like.
We didn't want to block like the initial configuration of the SDK. With this kind of stuff, but we also didn't want to like
have a have a release without this being thought through. So I think, like we have a path that you could do this, whether it is
going to happen. I think
there's there's a strong motivation to make it happen. But I think that, like if you, if you think very much the opposite, like, we can still address that in the future.
**David Ashpole** 40:36 Sure.
**Tyler Yahn** 40:41 Cool. Robert's already eaten. That means we're more than halfway through. So I'm gonna take another look at this. I will open up some issues. I probably won't get to it till early next week, David, which is unfortunate. I probably should prioritize that a little more. But
I'll ping you in slack or via Github. Once once I get around to it. Okay.
**David Ashpole** 41:02 Sounds good.
**Tyler Yahn** 41:04 Okay, perfect.
Okay. Looking back at the doc, I don't see anything else in the agenda.
thanks for taking notes. Whoever put that down, and then any other topics we want to talk about before we close it here.
I think there might be one more day to submit a talk to the observability day at Coupon, North America, by the way, so if you had something lingering, it's worth worth submitting.
But yeah, other than that, we could probably end it here. Oh, actually.
I guess we have some time. So I had this kind of harebrained idea. There's a request in the Evpf like auto instrumentation project for
for adding, like some sort of way to like dynamically set resource detectors on the startup. It's kind of a flawed proposal, but anyways, it got me thinking about like, can we provide some sort of solution here? And so we already have, like the auto export and the auto prop packages. I was looking at, creating something like an auto detector package
that you can essentially like. I think we already do this actually, in the hotel config. So this would be reused there, but essentially set up, like, you know, if you want one of our bundle detectors, you could set that up, and then you could also do like a register pathway as well.
I didn't know what people's appetites for. That would be, so. I wanted to maybe just
get a proposal together and then show it to you. But since we're on the call and we've got time, I just would maybe asking like, if that makes sense to people.
**Sam** 42:42 I think that would be good. I know some of the detector are kind of internal use, only we cannot even use externally. So the one of the practical thing I use is, I just initialize the resource and kind of export it, and found into another resource, which is
is not that useful.
**Tyler Yahn** 43:06 Yeah. Yeah. And that's kind of what like, the suggestion is right now for the auto export. It's like, essentially, just give us the attributes you go do the detection beforehand.
but I think it becomes a little bit harder for something that's designed to be 0 code. To then say like, go write your own essentially and come in. But yeah.
okay, I'll I'll get a proposal together or a Pr. Together, and I'll send it up.
**Robert Pająk** 43:32 I have also one question to some, because I think it's also related to our project. I saw some that you have been involved in the cementing database, semantic conventions.
propagation, and you also made some prototype into auto into your auto? SQL.
Package.
And my question is, do you need any support here. Do you want to look nice? And yeah, what is the status of it? etc?
So I just asking if you need any help. Basically, 1st of all.
**Sam** 44:07 Yeah, I mean, and
for now there is no like directly support is needed. But yeah, it would be great. Someone could take a look, especially at the
the proposal.
**Robert Pająk** 44:25 Because if that if others don't know what you're talking about, basically, there is a proposal
to add basically context, propagate, trace, trace, propagation or basically any propagation
for the database calls, so that if a database engine is or some plugin is able to detect, you know, Parse, basically, you know something from the from the database command, SQL, create or whatever. Then it's able to also kind of handle context propagation, or is is my explanation correct? Sam.
**Sam** 45:02 Kind of correct, because the current proposal only works for sequel server.
It's now like for every database.
Unfortunately that, that's because the Seco protocol is very limited. There is no headers could be attached.
So one of the way we can do this is by using SQL. Commenter, which is adding comments to the SQL. And let it propagate. But some database cannot accept that. Like SQL. Server, you could just break SQL. Server. So there is another trade off to use set context, which is a quite unique thing to the SQL. Server to make it
propagate the trace. But I I think this is still in the very early stage.
and I probably can ping you guys once it's more mature.
**Tyler Yahn** 45:54 Yeah. Sounds good. Let's plan on taking a look in the future.
**Sam** 45:58 Yeah.
**Tyler Yahn** 45:58 Okay.
Well, cool. Thanks. Everyone for joining. Appreciate, taking the time all the work that's being done. Also. Thanks again, Robert, for getting that release out, also appreciated. Forget to say that at the beginning. Yeah, that was that was helpful.
**Robert Pająk** 46:11 I was. I was having one question for the release. I almost forgot
the release part about signing you added it to open territory. Go, only not to contribute the description. Is it only because it should be added to contribute as well, or you did not need it there. I do done it for both. But I just was thinking about.
**Tyler Yahn** 46:31 Do do it for both. I just did it to.
Yeah, that was just a mistake. It should should be in both. We should probably update docs and everything. I was trying to get the slo or clothing. And then I yeah, all of those changes should eventually get migrated also to contribute. So that's a that's a great idea. Yeah, if if you wanted to go ahead and open up a Pr to just update the releasing docs there as well. That'd be great
that I didn't do it. But yeah.
also, thanks to the Pr. For the A test shell script as well. I took a look at that really quick. Yeah.
**Robert Pająk** 47:04 Okay.
**Tyler Yahn** 47:06 Yeah, I'm glad it worked. I'm glad it wasn't just working on my machine. Yeah.
**Robert Pająk** 47:12 As soon as you put, you know.
**Tyler Yahn** 47:15 Oh, yeah, that's true. Yeah, because the person does it on. Mac is going to be the harder one. Yeah, or windows.
Okay, everyone. We'll talk to you later.
**Robert Pająk** 47:24 Bye, bye.
